from .api_module import ApiModule


class Status(ApiModule):
    __slots__ = ()

    def get(self, user_id=None, group_id=None):
        return self._get_response(locals())

    def set(self, text=None, group_id=None):
        return self._get_response(locals())
