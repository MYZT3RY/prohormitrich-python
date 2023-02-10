from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML

def cmdSettings(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id
    args = context.args

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select * from `{0}` where `chatid` = '{1}'".format(dbConfig.tblChatSettings, tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    string = None

    if len(args) < 1:
        anekBg_string = 'включено' if row["show_anek_bg"] == 1 else 'выключено'

        string = "<b>Значения настроек чата</b>\n\nОтображение картинок в анекдотах (anekbg) - <b>{0}</b>\n\nЧтобы изменить параметр, введите команду и аргумент.".format(anekBg_string)
    elif args[0] == 'anekbg':
        row["show_anek_bg"] = not row["show_anek_bg"]

        cursor.execute("update `{0}` set `show_anek_bg` = '{1}' where `chatid` = '{2}'".format(dbConfig.tblChatSettings, int(row["show_anek_bg"]), tgChatId))

        anekBg_string = 'включено' if row["show_anek_bg"] == 1 else 'выключено'

        string = 'Отображение картинок в анекдотах <b>{0}</b>.'.format(anekBg_string)
    
    db.commit()
    db.close()

    if string is not None:
        context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)