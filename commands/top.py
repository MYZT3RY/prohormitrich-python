from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML

def cmdTop(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    tgChatId = update.message.chat_id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select`username`,`messages`,DATEDIFF(NOW(),`dateofregister`)as`days`,`userid`from`{0}`where`chatid`='{1}'order by`messages`desc limit 10".format(dbConfig.tblUsers,tgChatId))
    rows = cursor.fetchall()
    
    string = "<b>Рейтинг участников чата</b>\n\n"

    count = 0

    for row in rows:
        count = count + 1

        if row["days"] == 0:
            row["days"] = 1

        messagesPerDay = row["messages"] / row["days"]

        cursor.execute("call getNickname({0},{1})".format(row["userid"],tgChatId))
        stored_rows = cursor.fetchall()
        stored_row = stored_rows[0]

        username = row["username"]

        if stored_row["name"] is not None and stored_row["visible"]:
            username = stored_row["name"]

        tmp = "{0}. <b><u><a href='tg://'>{2}</a></u></b> ({3} сообщений, {4:.2f} сообщений в день)\n".format(count,row["userid"],username,row["messages"],messagesPerDay)
        string = string + tmp

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)