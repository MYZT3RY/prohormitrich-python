from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from telegram.constants import PARSEMODE_HTML
from configs import dbConfig

def cmdAll(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id

    username = update.message.from_user.username

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("call getNickname({0},{1})".format(tgUserId,tgChatId))
    stored_rows = cursor.fetchall()
    stored_row = stored_rows[0]

    if stored_row["name"] is not None and stored_row["visible"]:
        username = stored_row["name"]

    string = "<b><a href='tg://user?id={0}'>{1}</a></b> вызывает всех участников чата:\n\n".format(tgUserId,username)

    cursor.execute("select`userid`,`username`from`{0}`where`chatid`='{1}'".format(dbConfig.tblUsers,tgChatId))
    rows = cursor.fetchall()

    if len(rows) == 1:
        string = "Недостаточно участников в чате, чтобы использовать эту команду!"
    else:
        for row in rows:
            if row["userid"] != str(tgUserId):
                cursor.execute("call getNickname({0},{1})".format(row["userid"],tgChatId))
                stored_rows = cursor.fetchall()
                stored_row = stored_rows[0]

                username = row["username"]

                if stored_row["name"] is not None and stored_row["visible"]:
                    username = stored_row["name"]

                string = string + "<b><a href='tg://user?id={0}'>{1}</a></b>\n".format(row["userid"],username)

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML)