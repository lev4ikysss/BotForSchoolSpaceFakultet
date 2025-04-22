"""Логика работы приложения"""
import os
from utils.vk_utils import *
from utils.tg_utils import *
from utils.utils import *

class BotLogic :
    """
        Логика работы бота
        argument - :user_id: - int, id пользователя
        argument - :session: - str, "VK" или "TG" тип сессии
    """
    def __init__(self, user_id: int, session: str) :
        if not session in ["VK", "TG"] :
            return 1
        self.id = user_id
        self.session = session
        if session == "VK":
            self.vk = VkMethod(os.getenv('VK_TOKEN'))
        else :
            self.tg = TgMethod(os.getenv('TG_TOKEN'))

    def start(self) -> int :
        """
            Функция для запуска бота
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            message = "Здравствуйте!"
            if self.session == "VK" :
                self.vk.send_message(self.id, message)
                
            return 0
        except :
            return 1