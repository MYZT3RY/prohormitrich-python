from ast import Call
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
from commands import help
from commands import updates
from commands import top
from commands import nick
from commands import all
from configs import config
from configs import dbConfig

def message_handler(update: Update, context: CallbackContext):
    counter.messageCounter(update)

def main():
    updater = None

    try:
        updater = Updater(token=tgConfig.tgToken,use_context=True)

        print('Prohor Mitrich Bot started')

    except Exception as ex:
        print(ex)

    updater.dispatcher.add_handler(CommandHandler("all", all.cmdAll))
    updater.dispatcher.add_handler(CommandHandler("nick_visible", nick.cmdNick))
    updater.dispatcher.add_handler(CommandHandler("nick_delete", nick.cmdNick))
    updater.dispatcher.add_handler(CommandHandler("nick_show", nick.cmdNick))
    updater.dispatcher.add_handler(CommandHandler("nick_new", nick.cmdNick))
    updater.dispatcher.add_handler(CommandHandler("nick", nick.cmdNick))
    updater.dispatcher.add_handler(CommandHandler("top", top.cmdTop))
    updater.dispatcher.add_handler(CommandHandler("updates", updates.cmdUpdates))
    updater.dispatcher.add_handler(CommandHandler("help", help.cmdHelp))
    updater.dispatcher.add_handler(CommandHandler("mystats", mystats.cmdMyStats))
    updater.dispatcher.add_handler(CommandHandler("stats", stats.cmdStats))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    db = dbconnect.dbConnect()
    cursor = db.cursor()

    cursor.execute("select count(`id`)as `totalvalue`from`{0}`".format(dbConfig.tblNicknames))
    rows = cursor.fetchall()
    row = rows[0]

    config.valueOfNicknames = row["totalvalue"]

    db.close()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()