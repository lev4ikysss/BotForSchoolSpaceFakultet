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
        argument - :fakultet_id: - int, id факультета
        argument - :sign: - str, Токен пользователя вк для работы с талантами
        argument - :url: - str, URL ведущий на таланты
    """
    def __init__(self, user_id: int, session: str, fakultet_id: int, sign: str, url: str) :
        if not session in ["VK", "TG"] :
            return 1
        self.id = user_id
        self.session = session
        self.id_fakultet = fakultet_id
        if session == "VK":
            self.vk = VkMethod(os.getenv('VK_TOKEN'))
            self.vk_utils = VKUtils(os.getenv('VK_TOKEN'))
        else :
            self.tg = TgMethod(os.getenv('TG_TOKEN'))
        self.utils = Utils()
        self.tallants_utils = TallantUtils(sign, url)

    def start(self) -> int :
        """
            Функция для запуска бота
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            message = "Здравствуйте! Вы используете бота факультета МАМБА!"
            message_fail = "Вы не являетесь пользователем факультета!"
            message_error0 = "Произошла ошибка!"
            message_error1 = "Вы уже зарегистрированы!"
            message_success = "Поздравляю! Вы успешно зарегистрировались в боте!"
            if self.session == "VK" :
                self.vk.send_message(self.id, message)
                if not self.utils.check_reg(self.session, self.id) :
                    if not self.tallants_utils.check_member(self.id, self.id_fakultet) :
                        self.vk.send_message(self.id, message_fail)
                        return 1
                    tmp = self.utils.add_user(self.id)
                    if tmp == 1 :
                        self.vk.send_message(self.id, message_error0)
                        del(tmp)
                        return 1
                    del(tmp)
                    self.vk.send_message(self.id, message_success)
                else :
                    self.vk.send_message(self.id, message_error1)
                if self.utils.check_permissions(self.session, self.id) :
                    self.vk_utils.menu_admin(self.id)
                else :
                    self.vk_utils.menu(self.id)
            elif self.session == "TG" :
                pass
                # Для ТГ
            return 0
        except :
            return 1
        
    def menu(self) -> int :
        """
            Функция для вызова меню
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            message_error = "Вы не зарегистрированы!"
            if self.session == "VK" :
                if not self.utils.check_reg(self.session, self.id) :
                    self.vk.send_message(self.id, message_error)
                    return 1
                if self.utils.check_permissions(self.session, self.id) :
                    self.vk_utils.menu_admin(self.id)
                else :
                    self.vk_utils.menu(self.id)
            elif self.session == "TG" :
                pass
                # Для ТГ
            return 0
        except :
            return 1