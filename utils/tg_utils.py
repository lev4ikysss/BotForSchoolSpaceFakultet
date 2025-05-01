import telebot

class TgMethod:
    """
        Функции для работы с ТГ
        argument - :token: - str, токен для работы в тг
    """
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)

    def send_message(self, chat_id: int, message: str) -> int:
        """
            Отправка сообщения пользователю в ТГ
            argument - :chat_id: - int, id чата/пользователя ТГ, куда необходимо отправить сообщение
            argument - :message: - str, сообщение которое будет отправлено в чат/пользователю
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try:
            self.bot.send_message(chat_id=chat_id, text=message)
            return 0
        except:
            return 1

    def send_keyboard(self, chat_id: int, message: str, keyboard: list) -> int:
        """
            Отправка сообщения в чат в ТГ
            argument - :chat_id: - int, id чата/пользователя ТГ, куда необходимо отправить сообщение
            argument - :message: - str, сообщение которое будет отправлено в чат/пользователю
            argument - :keyboard: - list, список с описанием клавиатуры
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try:
            reply_markup = telebot.types.ReplyKeyboardMarkup(keyboard)
            self.bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
            return 0
        except:
            return 1