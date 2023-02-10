from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML

def cmdUpdates(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("\
        select \
            `text` \
            , date_format(create_date, '%\d.%\m.%\Y') as date \
        from \
            `{0}` \
        order by \
            `id` desc \
        limit 5 \
    ".format(dbConfig.tblUpdates))
    rows = cursor.fetchall()
    
    string = ""

    for row in rows:
        text = str(row["text"]).split("</b>")
        result = text[0] + " - " + row["date"] + "</b>" + text[1]

        string = string + "{0}\n\n".format(result)

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)