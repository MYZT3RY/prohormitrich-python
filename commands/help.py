from telegram import Update
from telegram.ext import CallbackContext
from messages import counter

def cmdHelp(update: Update, context: CallbackContext):
    counter.messageCounter(update)

    tgChatId = update.message.chat_id

    context.bot.send_message(chat_id=tgChatId, text="Список доступных команд\n\n/stats - просмотр статистики чата\n/mystats - просмотр личной статистики в чате")