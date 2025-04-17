"""Прочие утилиты"""
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
import vk_utils

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