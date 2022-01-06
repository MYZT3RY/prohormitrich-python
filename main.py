from telegram import Update, bot, chat, update, user
import telegram
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from configs import tgConfig
from commands import stats
from db import dbconnect
from messages import counter
from commands import mystats

def message_handler(update: Update, context: CallbackContext):
    counter.messageCounter(update)

def main():
    updater = None

    try:
        updater = Updater(token=tgConfig.tgToken,use_context=True)

        print('Prohor Mitrich Bot started')

    except Exception as ex:
        print(ex)

    updater.dispatcher.add_handler(CommandHandler("mystats", mystats.cmdMyStats))
    updater.dispatcher.add_handler(CommandHandler("stats", stats.cmdStats))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    db = dbconnect.dbConnect()
    db.close()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()