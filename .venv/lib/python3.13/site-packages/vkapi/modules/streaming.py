from .api_module import ApiModule


class Streaming(ApiModule):
    __slots__ = ()

    def getServerUrl(self):
        return self._get_response(locals())

    def getSettings(self):
        return self._get_response(locals())

    def getStats(self, _type=None, interval='5m', start_time=None, end_time=None):
        return self._get_response(locals())

    def getStem(self, word):
        return self._get_response(locals())

    def setSettings(self, monthly_tier=None):
        return self._get_response(locals())
