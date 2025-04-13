from .api_module import ApiModule


class Execute(ApiModule):
    __slots__ = ()

    def __call__(self, code):
        return self._get_response_execute(code)
