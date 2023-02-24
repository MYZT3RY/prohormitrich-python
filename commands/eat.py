from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML
import random
from configs import config
from functions import time_convert

def cmdEat(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("\
        select \
	        fl.food \
	        , floor(rand() * (fl.max_food_value - fl.min_food_value + 1) + fl.min_food_value) as rand_value \
        from \
	        food_list fl \
        order by \
	        rand() \
        limit 1 \
    ")

    rows = cursor.fetchall()
    food = rows[0]

    cursor.execute("\
        select \
            u.food_eated \
            , n.name \
            , u.nicknamevisible \
            , ( \
                case \
                    when unix_timestamp() >= u.food_timeout \
                        then true \
                    else false \
                end \
            ) as can_eat \
            , abs(u.food_timeout - unix_timestamp()) as timeout_left \
        from \
            {0} u \
                left join {1} n on n.id = u.nicknameid \
        where \
            u.userid = '{2}' \
            and u.chatid = '{3}' \
    ".format(dbConfig.tblUsers, dbConfig.tblNicknames, tgUserId, tgChatId))

    rows = cursor.fetchall()
    result = rows[0]

    username = update.message.from_user.username

    if result["nicknamevisible"]:
        username = result["name"]

    if result["can_eat"] == 1:
        result["food_eated"] += food["rand_value"]

        difference = 'увеличилась' if food["rand_value"] >= 1 else 'уменьшилась'

        string = "<b>{0}</b> съел {1}, сытость <b>{2}</b> на <b>{3:.0f} ед.</b>. Ваша сытость равна <b>{4:.0f} ед.</b>".format(username, food["food"], difference, food["rand_value"], result["food_eated"])

        query = "update `{0}` set `food_eated` = '{1}', `food_timeout` = unix_timestamp() + {2} where `userid` = '{3}' and `chatid` = '{4}'".format(dbConfig.tblUsers, result["food_eated"], config.foodTimeout, tgUserId, tgChatId)
        cursor.execute(query)

        db.commit()
    else:
        string = "<b>{0}</b>, следующий приём порции еды будет доступен через <b>{1}</b>".format(username, time_convert.time_left(result["timeout_left"]))

    cursor.close()
    db.close()

    if string is not None:
        context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)