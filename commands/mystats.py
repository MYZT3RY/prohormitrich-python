from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML

def cmdMyStats(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id
    tgChatName = update.message.chat.title

    cursor.execute("\
        select \
            u.* \
            , datediff(now(), u.dateofregister) as days \
            , date_format(u.dateofregister, '%\d.%m.%Y %H:%\i') as dateOfRegister \
        from \
            {0} u \
        where \
            u.userid = '{1}' \
            and u.chatid = '{2}' \
    ".format(dbConfig.tblUsers, tgUserId, tgChatId))

    rows = cursor.fetchall()
    row = rows[0]

    if row["days"] == 0:
        row["days"] = 1

    messagesPerDay = row["messages"] / row["days"]

    cursor.close()
    db.close()

    context.bot.send_message(chat_id=tgChatId, text="<b>Личная статистика в чате - {0}</b>\n\nДата регистрации в чате: <b>{1}</b>\n\nСообщений: <b>{2}</b>\nГолосовых сообщений: <b>{3}</b>\nВидео сообщений: <b>{4}</b>\nВидеозаписи: <b>{5}</b>\nАудиозаписи: <b>{6}</b>\nФотографий: <b>{7}</b>\nДокументов: <b>{8}</b>\nСтикеров: <b>{9}</b>\n\nСреднее количество сообщений в день: <b>{10:.2f}</b>".format(tgChatName,row["dateOfRegister"],row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],messagesPerDay), parse_mode=PARSEMODE_HTML, disable_notification=True)