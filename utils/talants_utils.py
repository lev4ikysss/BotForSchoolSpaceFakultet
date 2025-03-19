"""Утилиты для работы с API приложения Таланты"""
import requests

class TallantsAPI :
    """
        Работа с API приложения Академбазы - "Таланты"
    """
    def __init__(self, token: str) :
        """
            Получение токена пользователя зарегистрированных в приложении "Таланты"
            argument - :token: - str - Токен пользователя вк
        """
        self.access_token = token
