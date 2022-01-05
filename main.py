from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from configs import tgConfig
from configs import dbConfig
import pymysql

def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Тестовое сообщение',
    )

def main():
    updater = None

    try:
        updater = Updater(
            token=tgConfig.tgToken,
            use_context=True,
        )

        print('Prohor Mitrich Bot started')

    except Exception as ex:
        print(ex)

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))        

    db = dbConnect()
    db.close()

    updater.start_polling()
    updater.idle()

def dbConnect():
    dbHandle = None
    try:
        dbHandle = pymysql.connect(
            host=dbConfig.dbHostname,
            user=dbConfig.dbUsername,
            password=dbConfig.dbPassword,
            database=dbConfig.dbDatabase,
        )
        print('MySQL: Connected')

    except Exception as ex:
        print('MySQL: Connection failed')
        print(ex)

    return dbHandle

if __name__ == '__main__':
    main()