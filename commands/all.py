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

    cursor.execute("\
        select \
            u.userid \
            , u.username \
            , u.nicknamevisible \
            , n.name \
        from \
            {0} u \
                left join nicknames n on n.id = u.nicknameid \
        where \
            u.chatid = '{1}' \
    ".format(dbConfig.tblUsers,tgChatId))

    rows = cursor.fetchall()
    db.close()

    if len(rows) == 1:
        string = "Недостаточно участников в чате, чтобы использовать эту команду!"
    else:
        for i in range(len(rows)):
            if rows[i]["userid"] is not None and rows[i]["nicknamevisible"]:
                username= rows[i]["userid"]
                break

        string = "<b><a href='tg://user?id={0}'>{1}</a></b> вызывает всех участников чата:\n\n".format(tgUserId,username)

        for row in rows:
            if row["userid"] != str(tgUserId):
                username = row["username"]

                if row["name"] is not None and row["nicknamevisible"]:
                    username = row["name"]

                string = string + "<b><a href='tg://user?id={0}'>{1}</a></b>\n".format(row["userid"],username)

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML)