from .api_module import ApiModule


class Gifts(ApiModule):
    __slots__ = ()

    def get(self, user_id=None, count=None, offset=None):
        return self._get_response(locals())
