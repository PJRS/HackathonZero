# en el terminal windows:
# python -m pip install python-telegram-bot

from telegram.ext import Updater, CommandHandler
def main():
    updater = Updater(token="./bot_token", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repit", repit))
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    updater.start_polling()
    updater.idle()
def start(update, context):
    update.message.reply_text("Bienvenido, soy tu bot personal")
def repit(update, context):
    update.message.reply_text("Bienvenido, soy tu bot personal")
def suma(update, context):
    suma = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("La suma es: {}".format(suma))
main()