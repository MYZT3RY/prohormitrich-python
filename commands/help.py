from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML

def cmdHelp(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    tgChatId = update.message.chat_id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select`text`from`{0}`".format(dbConfig.tblHelp))
    rows = cursor.fetchall()
    
    string = "<b>Список доступных команд</b>\n\n"

    for row in rows:
        tmp = "{0}\n".format(row["text"])
        string = string + tmp

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)