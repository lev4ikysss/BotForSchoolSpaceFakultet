"""Прочие утилиты"""
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
import datetime
import json
import vk_utils
import tallants_utils

class VKUtils :
    """
        Доп. функции для работы с ВК сообществом
        argument - :token: - str, токен для работы в вк
    """
    def __init__(self, token: str) :
        self.vk = vk_utils.VkMethod(token)
    
    def menu(self, user_id: int) -> int :
        """
            Вызов меню для обычного пользователя
            argument - :user_id: - int, id пользователя ВК, которому необходимо отправить меню
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            self.vk.send_keyboard(user_id, "Открываю меню!", (
                Keyboard(one_time=False, inline=False)
                .add(OpenLink("https://vk.com/app8038390", "Таланты"))
                .row()
                .add(Text("Помощь"), color=KeyboardButtonColor.PRIMARY)
                .add(Text("Обо мне"), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Вызвать администратора"), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("Я нашёл баг!"), color=KeyboardButtonColor.POSITIVE)
                ).get_json())
            return 0
        except :
            return 1
        
    def menu_admin(self, user_id: int) -> int :
        """
            Вызов меню для пользователя с расширенными правами
            argument - :user_id: - int, id пользователя ВК, которому необходимо отправить меню
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            self.vk.send_keyboard(user_id, "Открываю меню для администраторов!", (
                Keyboard(one_time=False, inline=False)
                .add(OpenLink("https://vk.com/app8038390", "Таланты"))
                .row()
                .add(Text("Помощь"), color=KeyboardButtonColor.PRIMARY)
                .add(Text("Обо мне"), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Получить справку для администратора"), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("Я нашёл баг, тупые вы devops!"), color=KeyboardButtonColor.POSITIVE)
                ).get_json())
            return 0
        except :
            return 1
        
class Utils :
    """
        Прочие утилиты для работы приложения
    """

    def get_id(session: str, user_id: int) -> int :
        """
            Получение нашего id по id соц. сети
            argument - :session: - "TG" or "VK" or "OUR", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
            answer - 0 <= answer < infinite - int, наш id
            answer - -1 - int, ошибка 
        """
        try :
            if session == "VK" :
                with open('data/vk_id.json', 'r') as file :
                    ident = json.load(file)
            elif session == "TG" :
                with open('data/tg_id.json', 'r') as file :
                    ident = json.load(file)
            elif session == "OUR" :
                return user_id
            else :
                return -1
            return ident[f'{user_id}']
        except :
            return -1

    def check_permissions(session: str, user_id: int) -> bool :
        """
            Проверка на наличие прав администратора у пользователя
            argument - :session: - "TG" or "VK" or "OUR", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
            answer - True - bool, пользователь является администратором
            answer - False - bool, пользователь не является администратором, или ошибка
        """
        try :
            id = Utils.get_id(session, user_id)
            with open('data/user_data.json', 'r') as file :
                users = json.load(file)
            return users[f'{id}']['is_admin']
        except :
            return False
        
    def change_permissions(session: str, user_id: int, change: bool) -> int :
        """
            Назначение статуса администратора пользователю
            argument - :session: - "TG" or "VK" or "OUR", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            id = Utils.get_id(session, user_id)
            with open('data/user_data.json', 'r') as file :
                users = json.load(file)
            users[f'{id}']['is_admin'] = change
            with open('data/user_data.json', 'w') as file :
                json.dump(users, file)
            return 0
        except :
            return 1
        
    def change_don(session: str, user_id: int, change: bool) -> int :
        """
            Назначение статуса дона пользователю
            argument - :session: - "TG" or "VK" or "OUR", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            id = Utils.get_id(session, user_id)
            with open('data/user_data.json', 'r') as file :
                users = json.load(file)
            users[f'{id}']['is_don'] = change
            with open('data/user_data.json', 'w') as file :
                json.dump(users, file)
            return 0
        except :
            return 1
        
    def change_prestige(session: str, user_id: int, change: bool) -> int :
        """
            Назначение статуса разработчика пользователю
            argument - :session: - "TG" or "VK" or "OUR", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            id = Utils.get_id(session, user_id)
            with open('data/user_data.json', 'r') as file :
                users = json.load(file)
            users[f'{id}']['is_develop'] = change
            with open('data/user_data.json', 'w') as file :
                json.dump(users, file)
            return 0
        except :
            return 1
        
    def add_user(user_id: int) -> int :
        """
            Добавление пользователя в базу данных, использовать только в вк
            argument - :user_id: - int, id пользователя
            answer - 0 - int, успех
            answer - 1 - int, ошибка
        """
        try :
            date = datetime.datetime.now()
            with open('data/user_data.json', 'r') as file :
                users = json.load(file)
            id = len(users.keys())
            users[f'{id}'] = {
                "ID_VK": user_id,
                "ID_TG": 0,
                "REG_DATE": {
                    "YEAR": date.year,
                    "MONTH": date.month,
                    "DAY": date.day,
                    "HOUR": date.hour,
                    "MINUTES": date.minute,
                    "SECOND": date.second
                },
                "is_admin": False,
                "is_don": False,
                "is_develop": False,
                "score": 0,
                "talant": {
                    "ID": 0,
                    "ROLE": "UNKNOWN",
                    "history": []
                }
            }
            with open('data/user_data.json', 'w') as file :
                json.dump(users, file)
            with open(f'data/vk_id.json', 'r') as file :
                pointer = json.load(file)
            pointer[f'user_id'] = id
            with open(f'data/vk_id.json', 'w') as file :
                json.dump(pointer, file)
            return 0
        except :
            return 1
        
    def check_reg(session: str, user_id: int) -> bool :
        """
            Проверить, зарегистрирован ли id
            argument - :session: - "TG" or "VK", тип сессии id пользователя
            argument - :user_id: - int, id пользователя
        """
        try :
            with open(f'data/{session.lower()}_id.json', 'r') as file :
                keys = json.load(file).keys()
            if str(user_id) in keys :
                return True
            return False
        except :
            return False
        
class TallantUtils :
    """
        Утилиты работающие с талантами
        argument - :sign: - str, Токен пользователя вк для работы с талантами
        argument - :url: - str, URL ведущий на таланты
    """
    def __init__(self, sign: str, url: str) :
        self.tallants = tallants_utils.TallantsAPI(sign, url)

    def check_member(self, user_id: int, fakultet_id: int) -> bool :
        """
            Проверить, является ли пользователь участником факультета
            argument - :user_id: - int, id пользователя VK
            argument - :fakultet_id: - int, id факультета
            answer - True - bool, пользователь является участником факультета
            answer - False - bool, пользователь не является участником факультета 
        """
        try :
            users = self.tallants.get_fakultet_by_id(fakultet_id)['response']['users']
            for user in users :
                if user['info']['id_vk'] == user_id :
                    return True
            return False
        except :
            return False