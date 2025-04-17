from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text('Привет!')

def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    application = ApplicationBuilder().token('7729497145:AAFCTIgmlXgtg7Ufbd5Ia6MWShnz624toec').build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler('start', start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
