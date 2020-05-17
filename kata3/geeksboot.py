from telegram.ext import Updater, CommandHandler


def main():
    #instanciamos el updater
    updater = Updater(token=open("").read(), use_context=True)
    
    #añadiendo un manejador al comnado /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #añadiendo un manejador al comnado /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #añadiendo un manejador al comnado /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #empezamos a pedir notificaciones a telegram
    updater.start_polling()

    #capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def start(update, context):
    # args = (2, 2)
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado es " + resultado)

