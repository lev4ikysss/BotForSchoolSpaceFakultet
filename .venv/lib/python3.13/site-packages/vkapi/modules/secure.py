from .api_module import ApiModule


class Secure(ApiModule):
    __slots__ = ()

    def set_client_secret(self, client_secret):
        self._params.update({'client_secret': client_secret})

    def addAppEvent(self, activity_id, user_id=None, value=None):
        return self._get_response(locals())

    def checkToken(self, token=None, ip=None):
        return self._get_response(locals())

    def getAppBalance(self):
        return self._get_response(locals())

    def getSMSHistory(self, user_id=None, date_from=None, date_to=None, limit=1000):
        return self._get_response(locals())

    def getTransactionsHistory(self):
        return self._get_response(locals())

    def getUserLevel(self, user_ids):
        return self._get_response(locals())

    def giveEventSticker(self, user_ids, achievement_id):
        return self._get_response(locals())

    def sendNotification(self, message, user_ids=None, user_id=None):
        return self._get_response(locals())

    def sendSMSNotification(self, user_id, message):
        return self._get_response(locals())

    def setCounter(self, counters=None, user_id=None, counter=None, increment=False):
        return self._get_response(locals())
