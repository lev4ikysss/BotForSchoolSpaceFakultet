import vk_api
import random

class VkMethod :
    """
        Функции для работы с ВК
    """
    def __init__(self, token: str) :
        self.vk = vk_api.VkApi(token=token)

    def send_message(self, user_id: int, message: str) -> int :
        """
            Отправка сообщения пользователю в ВК
            argument - :user_id: - int, id пользователя ВК, которому необходимо отправить сообщение
            argument - :message: - str, сообщение которое будет отправлено пользователю
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(1, 1000000000000)})
            return 0
        except :
            return 1
        
    def send_message_chat(self, chat_id: int, message: str) -> int :
        """
            Отправка сообщения в чат в ВК
            argument - :chat_id: - int, id чата ВК, куда необходимо отправить сообщение
            argument - :message: - str, сообщение которое будет отправлено в чат
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            self.vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': random.randint(1, 1000000000000)})
            return 0
        except :
            return 1
        
    def send_keyboard(self, user_id: int, message: str, keyboard: dict) -> int :
        """
            Отправка сообщения в чат в ВК
            argument - :user_id: - int, id пользователя ВК, которому необходимо отправить сообщение
            argument - :message: - str, сообщение которое будет отправлено в чат
            argument - :keyboard: - dict, словарь с описанием клавиатуры
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'keyboard': keyboard, 'random_id': random.randint(1, 1000000000000)})
            return 0
        except :
            return 1