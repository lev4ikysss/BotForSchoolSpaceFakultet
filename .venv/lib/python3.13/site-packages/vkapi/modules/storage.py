from .api_module import ApiModule


class Storage(ApiModule):
    __slots__ = ()

    def get(self, key=None, keys=None, user_id=None, _global=False):
        return self._get_response(locals())

    def getKeys(self, user_id=None, _global=False, offset=0, count=100):
        return self._get_response(locals())

    def set(self, key, value=None, user_id=None, _global=False):
        return self._get_response(locals())
