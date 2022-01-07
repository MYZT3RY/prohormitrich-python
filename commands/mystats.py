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

    cursor.execute("select*,DATEDIFF(NOW(),`dateofregister`)as`days`from`{0}`where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    if row["days"] == 0:
        row["days"] = 1

    messagesPerDay = row["messages"] / row["days"]

    cursor.close()
    db.close()

    context.bot.send_message(chat_id=tgChatId, text="<b>Личная статистика в чате</b>\n\nДата регистрации в чате: <b>{0}</b>\n\nСообщений: <b>{1}</b>\nГолосовых сообщений: <b>{2}</b>\nВидео сообщений: <b>{3}</b>\nВидеозаписи: <b>{4}</b>\nАудиозаписи: <b>{5}</b>\nФотографий: <b>{6}</b>\nДокументов: <b>{7}</b>\nСтикеров: <b>{8}</b>\n\nСреднее количество сообщений в день: <b>{9:.2f}</b>".format(row["dateofregister"],row["messages"],row["voices"],row["videovoices"],row["videos"],row["audios"],row["photos"],row["documents"],row["stickers"],messagesPerDay), parse_mode=PARSEMODE_HTML)