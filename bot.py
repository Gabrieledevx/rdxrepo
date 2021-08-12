from telegram.ext import Updater, CommandHandler,ConversationHandler
from scra import trend_today,categories_inlist
import selenium
#coment
#Selenium part

def start(update, context):

    update.message.reply_text('Bienvenido a Wissen')

def prueba_CommandHandler(update,context):
    update.message.reply_text('')

if __name__== '__main__':

        Updater = Updater(token='1719779312:AAGeZjG53miskDewKF8Riv9cTgeygSNjPpc',use_context=True)
       
        dp = Updater.dispatcher 
        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(ConversationHandler(
            entry_points=[
                CommandHandler('Trend',trend_today),
                CommandHandler('Categories',categories_inlist)

            ],
            states={},
            fallbacks=[]
        ))
        #handler 
        Updater.start_polling()
        Updater.idle()

