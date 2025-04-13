from .api_module import ApiModule


class Utils(ApiModule):
    __slots__ = ()

    def checkLink(self, url):
        return self._get_response(locals())

    def deleteFromLastShortened(self, key):
        return self._get_response(locals())

    def getLastShortenedLinks(self, count=10, offset=0):
        return self._get_response(locals())

    def getLinkStats(self, key, source='vk_cc', access_key=None, interval='day', interval_count=1, extended=False):
        return self._get_response(locals())

    def getServerTime(self):
        return self._get_response(locals())

    def getShortLink(self, url, private=False):
        return self._get_response(locals())

    def resolveScreenName(self, screen_name):
        return self._get_response(locals())
