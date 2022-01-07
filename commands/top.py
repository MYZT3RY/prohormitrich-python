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

    cursor.execute("select`username`,`messages`,DATEDIFF(NOW(),`dateofregister`)as`days`from`{0}`where`chatid`='{1}'order by`messages`desc limit 10".format(dbConfig.tblUsers,tgChatId))
    rows = cursor.fetchall()
    
    string = "<b>Рейтинг участников чата</b>\n\n"

    count = 0

    for row in rows:
        count = count + 1

        if row["days"] == 0:
            row["days"] = 1

        messagesPerDay = row["messages"] / row["days"]

        tmp = "{0}. <b>@{1}</b> ({2} сообщений, {3:.2f} сообщений в день)\n".format(count,row["username"],row["messages"],messagesPerDay)
        string = string + tmp

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML)