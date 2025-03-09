from imports import *
import handlers

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext

# Main function
def main():
  application = Application.builder().token(BOT_TOKEN).build()


  conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", handlers.start)],
        states={
            handlers.NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND,  handlers.get_name)],
            handlers.SURNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND,  handlers.get_surname)],
            handlers.EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND,  handlers.get_email)],
            handlers.PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND,  handlers.get_phone)],
            handlers.CONFIRM: [MessageHandler(filters.Regex("^(Yes|No)$"),  handlers.confirm)],
        },
        fallbacks=[CommandHandler("cancel", handlers.cancel)],
    )

  application.add_handler(conv_handler)

  # Start the bot
  application.run_polling()

if(__name__ == "__main__"):
  main()
