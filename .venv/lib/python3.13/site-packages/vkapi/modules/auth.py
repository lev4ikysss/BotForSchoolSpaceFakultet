from .api_module import ApiModule


class Auth(ApiModule):
    __slots__ = ()

    def checkPhone(self, phone, client_id=None, client_secret=None, auth_by_phone=False):
        return self._get_response(locals())

    def restore(self, phone, last_name):
        return self._get_response(locals())
