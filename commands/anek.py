import random
from telegram import Update
from telegram.ext import CallbackContext
from messages import counter
from telegram.constants import PARSEMODE_HTML
import requests
from bs4 import BeautifulSoup
from configs import config
from configs import dbConfig
from db import dbconnect

def cmdAnek(update: Update, context: CallbackContext):
    counter.messageCounter(update.message)

    tgChatId = update.message.chat_id

    response = requests.get(config.urlAnek)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'lxml')
    numberOfAnek = soup.find('h2').text.strip()
    result = soup.find('p').text.strip()

    randPhoto = random.randint(1, config.valueOfAnekBg)
    photoPath = open("{0}{1}{2:02}.jpg".format(config.pathToAnekBg, config.prefixAnekBg, randPhoto), 'rb')
    
    string = "\n<i><b>{0}</b></i>\n\n{1}\n".format(numberOfAnek, result)

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select `show_anek_bg` from `{0}` where `chatid` = '{1}'".format(dbConfig.tblChatSettings, tgChatId))
    rows = cursor.fetchall()
    row = rows[0]

    if row["show_anek_bg"] == 1:
        context.bot.send_photo(chat_id=tgChatId, photo=photoPath, caption=string, parse_mode=PARSEMODE_HTML, disable_notification=True)
    else:
        context.bot.send_message(chat_id=tgChatId, text=string, parse_mode=PARSEMODE_HTML, disable_notification=True)