from .api_module import ApiModule


class Notifications(ApiModule):
    __slots__ = ()

    def get(self, count=30, start_from=None, filters=None, start_time=None, end_time=None):
        return self._get_response(locals())

    def markAsViewed(self):
        return self._get_response(locals())

    def sendMessage(self, user_ids, message, fragment=None):
        return self._get_response(locals())
