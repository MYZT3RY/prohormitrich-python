from telegram import Update, bot
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from configs import tgConfig
from telegram.constants import PARSEMODE_HTML

def cmdStats(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    tgChatId = update.message.chat_id
    tgChatName = update.message.chat.title

    cursor.execute("\
        select \
            c.* \
            , date_format(c.dateofregister, '%\d.%\m.%Y %H:%\i') as dateOfRegister \
            , datediff(now(), c.dateofregister) as days \
            , (select count(u.id) from {0} u where u.chatid = c.id) as registeredusers \
        from \
            {1} c \
        where \
            c.id = '{2}' \
    ".format(dbConfig.tblUsers, dbConfig.tblChats, tgChatId))

    rows = cursor.fetchall()
    row = rows[0]

    if row["days"] == 0:
        row["days"] = 1

    messagesPerDay = row["messages"] / row["days"]

    cursor.close()
    db.close()

    totalUsers = bot.Bot(tgConfig.tgToken).getChatMemberCount(chat_id=tgChatId)

    context.bot.send_message(chat_id=tgChatId, text="<b>Статистика чата - {0}</b>\n\nДата регистрации чата: <b>{1}</b>\nКоличество участников чата: <b>{2}</b> (<b>{3}</b> зарегистрированных)\n\nСообщений: <b>{4}</b>\nГолосовых сообщений: <b>{5}</b>\nВидео сообщений: <b>{6}</b>\nВидеозаписи: <b>{7}</b>\nАудиозаписи: <b>{8}</b>\nФотографий: <b>{9}</b>\nДокументов: <b>{10}</b>\nСтикеров: <b>{11}</b>\nОтредактированных сообщений: <b>{12}</b>\n\nСреднее количество сообщений в день: <b>{13:.2f}</b>".format(tgChatName,row["dateOfRegister"],totalUsers,row["registeredusers"],row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],row["edited_messages"],messagesPerDay), parse_mode=PARSEMODE_HTML, disable_notification=True)