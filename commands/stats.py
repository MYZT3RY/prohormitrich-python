from telegram import Update, bot
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from configs import tgConfig
from telegram.constants import PARSEMODE_HTML

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

    context.bot.send_message(chat_id=tgChatId, text="<b>Статистика чата</b>\n\nДата регистрации чата: <b>{0}</b>\nКоличество участников чата: <b>{1}</b> (<b>{2}</b> зарегистрированных)\n\nСообщений: <b>{3}</b>\nГолосовых сообщений: <b>{4}</b>\nВидео сообщений: <b>{5}</b>\nВидеозаписи: <b>{6}</b>\nАудиозаписи: <b>{7}</b>\nФотографий: <b>{8}</b>\nДокументов: <b>{9}</b>\nСтикеров: <b>{10}</b>\n\nСреднее количество сообщений в день: <b>{11}</b>".format(row["dateofregister"],totalUsers,registeredUsers,row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],messagesPerDay), parse_mode=PARSEMODE_HTML)