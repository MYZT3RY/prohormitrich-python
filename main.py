from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
import configs.tgConfig

def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Тестовое сообщение',
    )

def main():
    print('Start')

    updater = Updater(
        token=configs.tgConfig.tgToken,
        use_context=True,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()