from telegram import Update, bot
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from configs import tgConfig

def cmdStats(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    tgChatId = update.message.chat_id

    cursor.execute("select count(`id`)as`registeredusers`from`{0}`where`chatid`='{1}'".format(dbConfig.tblUsers,tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    registeredUsers = row["registeredusers"]

    cursor.execute("select*,DATEDIFF(NOW(),`dateofregister`)as`days`from`{0}`where`id`='{1}'".format(dbConfig.tblChats,tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    if row["days"] == 0:
        row["days"] = 1

    messagesPerDay = row["messages"] / row["days"]

    cursor.close()
    db.close()

    totalUsers = bot.Bot(tgConfig.tgToken).getChatMemberCount(chat_id=tgChatId)

    context.bot.send_message(chat_id=tgChatId, text="Статистика чата\n\nДата регистрации чата: {0}\nКоличество участников чата: {1} ({2} зарегистрированных)\n\nСообщений: {3}\nГолосовых сообщений: {4}\nВидео сообщений: {5}\nВидеозаписи: {6}\nАудиозаписи: {7}\nФотографий: {8}\nДокументов: {9}\nСтикеров: {10}\n\nСреднее количество сообщений в день: {11}".format(row["dateofregister"],totalUsers,registeredUsers,row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],messagesPerDay))