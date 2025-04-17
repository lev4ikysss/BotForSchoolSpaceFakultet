import telebot

class TelegramBot:
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)

    def send_message(self, chat_id: int, message: str) -> int:
        try:
            self.bot.send_message(chat_id=chat_id, text=message)
            return 0
        except:
            return 1

    def send_keyboard(self, chat_id: int, message: str, keyboard: list) -> int:
        try:
            reply_markup = telebot.types.ReplyKeyboardMarkup(keyboard)
            self.bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
            return 0
        except:
            return 1

    def add_handler(self, command, function):
        self.bot.message_handler(commands=[command])(function)

    def run(self):
        self.bot.polling()

