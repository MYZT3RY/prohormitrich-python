from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML
import re

def cmdTop(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    command = update.message.text
    arg = ""

    if re.search(context.bot.name,command):
        command = command.replace(context.bot.name,"")

    if re.search("_",command):
        arg = command.rsplit("_")
    elif re.search(" ",command):
        arg = command.rsplit(" ")

    tgChatId = update.message.chat_id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    if len(arg) == 2 and arg[1] == "messages":
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
        
        string = "<b>Рейтинг участников чата по количеству сообщений.</b>\n\n"

        count = 0

        for row in rows:
            count = count + 1

            if row["days"] == 0:
                row["days"] = 1

            messagesPerDay = row["messages"] / row["days"]

            username = row["username"]

            if row["name"] is not None and row["visible"]:
                username = row["name"]

            tmp = "{0}. <b><u>{1}</u></b> (<b>{2}</b> сообщений, <b>{3:.2f}</b> сообщений в день)\n".format(count, username, row["messages"], messagesPerDay)
            string = string + tmp
    elif len(arg) == 2 and arg[1] == "vodka":
        cursor.execute("\
            select \
                u.username \
                , u.userid \
                , u.nicknamevisible as visible \
                , n.name \
                , u.vodka_drinked \
            from \
                {0} u \
                    left join {1} n on n.id = u.nicknameid \
            where \
                u.chatid = '{2}' \
                and u.vodka_drinked <> '0' \
            order by \
                u.vodka_drinked desc \
            limit 10 \
        ".format(dbConfig.tblUsers, dbConfig.tblNicknames, tgChatId))

        rows = cursor.fetchall()
        
        string = "<b>Рейтинг участников чата по количеству выпитой водки.</b>\n\n"

        count = 0

        for row in rows:
            count = count + 1

            username = row["username"]

            if row["name"] is not None and row["visible"]:
                username = row["name"]

            tmp = "{0}. <b><u>{1}</u></b> (<b>{2:.1f} л.</b>)\n".format(count, username, row["vodka_drinked"])
            string = string + tmp
    elif len(arg) == 2 and arg[1] == "eat":
        cursor.execute("\
            select \
                u.username \
                , u.userid \
                , u.nicknamevisible as visible \
                , n.name \
                , u.food_eated \
            from \
                {0} u \
                    left join {1} n on n.id = u.nicknameid \
            where \
                u.chatid = '{2}' \
                and u.food_eated <> '0' \
            order by \
                u.food_eated desc \
            limit 10 \
        ".format(dbConfig.tblUsers, dbConfig.tblNicknames, tgChatId))

        rows = cursor.fetchall()
        
        string = "<b>Рейтинг участников чата по количеству сытости.</b>\n\n"

        count = 0

        for row in rows:
            count = count + 1

            username = row["username"]

            if row["name"] is not None and row["visible"]:
                username = row["name"]

            tmp = "{0}. <b><u>{1}</u></b> (<b>{2} ед.</b>)\n".format(count, username, row["food_eated"])
            string = string + tmp
    else:
        string = "Команда имеет следующие аргументы:\n\n<i>/top_messages</i> <b>(messages)</b> - отобразить топ по сообщениям.\n<i>/top_vodka</i> <b>(vodka)</b> - отобразить топ по количеству выпитой водки.\n<i>/top_eat</i> <b>(eat)</b> - отобразить топ по количеству сытости."
    
    db.close()

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)