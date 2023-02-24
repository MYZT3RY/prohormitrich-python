from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML
import random
from configs import config
from functions import time_convert

def cmdVodka(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("\
        select \
	        u.vodka_drinked \
	        , n.name \
	        , u.nicknamevisible \
            , ( \
                case \
                    when unix_timestamp() >= u.vodka_timeout \
                        then true \
                    else false \
                end \
            ) as can_drink \
            , abs(u.vodka_timeout - unix_timestamp()) as timeout_left \
        from \
	        users u \
		        left join nicknames n on n.id = u.nicknameid \
        where \
            u.userid = '{1}' \
            and u.chatid = '{2}' \
    ".format(dbConfig.tblUsers, tgUserId, tgChatId))

    rows = cursor.fetchall()
    result = rows[0]

    username = update.message.from_user.username

    if result["nicknamevisible"]:
        username = result["name"]

    if result["can_drink"] == 1:
        vodkaDrinkedRandom = random.uniform(config.minVodkaDrink, config.maxVodkaDrink)
        result["vodka_drinked"] += vodkaDrinkedRandom

        string = "<b>{0}</b> выпил <b>{1:.1f} л.</b> водки. Всего выпито <b>{2:.1f} л.</b>".format(username, vodkaDrinkedRandom, result["vodka_drinked"])

        query = "update `{0}` set `vodka_drinked` = '{1}', `vodka_timeout` = unix_timestamp() + {2} where `userid` = '{3}' and `chatid` = '{4}'".format(dbConfig.tblUsers, result["vodka_drinked"], config.vodkaTimeout, tgUserId, tgChatId)
        cursor.execute(query)

        db.commit()
    else:
        string = "<b>{0}</b>, следующий приём порции водки будет доступен через <b>{1}</b>".format(username, time_convert.time_left(result["timeout_left"]))

    cursor.close()
    db.close()

    if string is not None:
        context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)