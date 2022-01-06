from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect

def cmdUpdates(update: Update, context: CallbackContext):
    tgChatId = update.message.chat_id

    counter.messageCounter(update)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select`text`from`updates`order by`id`desc limit 5")
    rows = cursor.fetchall()
    
    string = ""
    print(rows)

    for row in rows:
        print(row)
        tmp = "{0}\n\n".format(row["text"])
        string = string + tmp

    context.bot.send_message(chat_id=tgChatId, text=string)