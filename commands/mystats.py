from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig

def cmdMyStats(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id

    cursor.execute("select*,DATEDIFF(NOW(),`dateofregister`)as`days`from`{0}`where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    messagesPerDay = row["messages"] / row["days"]

    cursor.close()
    db.close()

    context.bot.send_message(chat_id=tgChatId, text="Личная статистика в чате\n\nДата регистрации в чате: {0}\n\nСообщений: {1}\nГолосовых сообщений: {2}\nВидео сообщений: {3}\nВидеозаписи: {4}\nАудиозаписи: {5}\nФотографий: {6}\nДокументов: {7}\nСтикеров: {8}\n\nСреднее количество сообщений в день: {9}".format(row["dateofregister"],row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],messagesPerDay))