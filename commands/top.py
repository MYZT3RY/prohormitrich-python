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

    cursor.execute("\
        select \
            u.username \
            , u.messages \
            , datediff(now(), u.dateofregister) as days \
            , u.userid \
            , u.nicknamevisible as visible \
            , n.name \
        from \
            {0} u \
                left join {1} n on n.id = u.nicknameid \
        where \
            u.chatid = '{2}' \
        order by \
            u.messages desc \
        limit 10 \
    ".format(dbConfig.tblUsers, dbConfig.tblNicknames, tgChatId))

    rows = cursor.fetchall()
    
    string = "<b>Рейтинг участников чата</b>\n\n"

    count = 0

    for row in rows:
        count = count + 1

        if row["days"] == 0:
            row["days"] = 1

        messagesPerDay = row["messages"] / row["days"]

        username = row["username"]

        if row["name"] is not None and row["visible"]:
            username = row["name"]

        tmp = "{0}. <b><u><a href='tg://'>{2}</a></u></b> (<b>{3}</b> сообщений, <b>{4:.2f}</b> сообщений в день)\n".format(count,row["userid"],username,row["messages"],messagesPerDay)
        string = string + tmp

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)