from ast import arg
from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from db import dbconnect
from configs import dbConfig
from telegram.constants import PARSEMODE_HTML
from uuid import uuid4

def cmdSettings(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id
    args = context.args

    key = 'settings' + str(tgChatId)

    if not (key in context.chat_data):
        context.chat_data[key] = {'anekbg': True, 'test':'ТЫ ХУЙ'}

    anekBg = context.chat_data[key]["anekbg"]

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    string = ''

    if len(args) < 1:
        anekBg_string = 'включено' if anekBg is True else 'выключено'

        string = "<b>Значения настроек чата</b>\n\nОтображение картинок в анекдотах (anekbg) - <b>{0}</b>".format(anekBg_string)
    elif args[0] == 'anekbg':
        anekBg = not anekBg

        context.chat_data[key]["anekbg"] = anekBg

        cursor.execute("update`chat_settings`set`show_anek_bg`='{0}'where`chatid`='{1}'".format(anekBg, tgChatId))

        anekBg_string = 'включено' if anekBg is True else 'выключено'

        string = 'Отображение картинок в анекдотах <b>{0}</b>.'.format(anekBg_string)
    
    db.commit()
    db.close()

    context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)