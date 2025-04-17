import telebot

API_TOKEN = ''
bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я ваш телеграм-бот!")

bot.polling()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

# Этот код отправит обратно все текстовые сообщения, которые получит бот.
