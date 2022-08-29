from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
import random
from configs import config
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML
import re

def cmdNick(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    command = update.message.text
    arg = ""

    if re.search(context.bot.name,command):
        command = command.replace(context.bot.name,"")

    if re.search("_",command):
        arg = command.rsplit("_")
    elif re.search(" ",command):
        arg = command.rsplit(" ")

    tgChatId = update.message.chat_id
    tgUserId = update.message.from_user.id

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    string = ""

    if len(arg) == 2 and arg[1] == "new":
        randValue = random.randint(1, config.valueOfNicknames)

        cursor.execute("select`name`from`{0}`where`id`='{1}'".format(dbConfig.tblNicknames, randValue))
        rows = cursor.fetchall()
        row = rows[0]

        cursor.execute("update`{0}`set`nicknameid`='{1}'where`userid`='{2}'and`chatid`='{3}'".format(dbConfig.tblUsers, randValue, tgUserId, tgChatId))

        string = "Ваш новый внутренний никнейм - <b>{0}</b>".format(row["name"])
    elif len(arg) == 2 and arg[1] == "show":
        cursor.execute("\
            select \
	            n.name \
	            , u.nicknamevisible as visible \
            from \
	            {0} u \
		            left join {1} n on n.id = u.nicknameid \
            where \
	            u.userid = '{2}' \
	            and u.chatid = '{3}' \
        ".format(dbConfig.tblUsers, dbConfig.tblNicknames, tgUserId, tgChatId))

        rows = cursor.fetchall()
        row = rows[0]

        if row["name"] == None:
            row["name"] = "не установлен"

        visibility = ""

        if row["visible"]:
            visibility = "отображается"
        else:
            visibility = "не отображается"

        string = "Ваш текущий внутренний никнейм - <b>{0}</b>\nРежим отображения никнейма - <b>{1}</b>".format(row["name"],visibility)
    elif len(arg) == 2 and arg[1] == "delete":
        cursor.execute("update`{0}`set`nicknameid`=default where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
        db.commit()
        result = db.affected_rows()

        if result:
            string = "Текущий внутренний никнейм удалён!"
        else:
            string = "Текущий внутренний никнейм не удалён, т.к. он не установлен!"
    elif len(arg) == 2 and arg[1] == "visible":
        cursor.execute("update`{0}`set`nicknamevisible`=not`nicknamevisible`where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
        db.commit()
        result = db.affected_rows()

        if result:
            cursor.execute("select`nicknamevisible`from`{0}`where`userid`='{1}'and`chatid`='{2}'".format(dbConfig.tblUsers,tgUserId,tgChatId))
            rows = cursor.fetchall()
            row = rows[0]

            if row["nicknamevisible"]:
                string = "Режим видимости никнейма - <b>отображается</b>"
            else:
                string = "Режим видимости никнейма - <b>не отображается</b>"
    else:
        string = "Команда имеет следующие аргументы:\n\n<i>/nick_new</i> <b>(new)</b> - выбрать новый рандомный внутренний никнейм.\n<i>/nick_show</i> <b>(show)</b> - отобразить текущий внутренний никнейм.\n<i>/nick_delete</i> <b>(delete)</b> - удалить текущий внутренний никнейм.\n<i>/nick_visible</i> <b>(visible)</b> - сменить режим отображения внутреннего никнейма."
    
    db.commit()
    db.close()

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)