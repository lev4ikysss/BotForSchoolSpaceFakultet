"""Утилиты для работы с API приложения Таланты"""
import requests

class TallantsAPI :
    """
        Работа с API приложения Академбазы - "Таланты"
        argument - :sign: - str, Токен пользователя вк для работы с талантами
        argument - :url: - str, URL ведущий на таланты
    """
    def __init__(self, sign: str, url: str) :
        self.sign = sign
        self.url = url
        self.request = {
            "vk_access_token_settings": None,
            "vk_app_id": 8038390,
            "vk_are_notifications_enabled": 0,
            "vk_is_app_user": 1,
            "vk_is_favorite": 0,
            "vk_is_recommended": 1,
            "vk_language": "en",
            "vk_platform": "desktop_web",
            "vk_ref": "other",
            "vk_ts": 1745167102,
            "vk_user_id": 1026360620,
            "sign": self.sign
        }
    
    def get_fakultet_by_id(self, id_fakultet: int) -> dict :
        """
            Получить информацию о факультете
            argument - :id_fakultet: - int, id факультета
            answer - :{"response": 1}: - dict, ошибка
            answer - :{"response": ...}: - dict, успех
        """
        try :
            req = self.request
            req['id'] = id_fakultet
            res = requests.get(f"{self.url}/clans.getClanById", req).json()
            return res
        except :
            return {"response": 1}