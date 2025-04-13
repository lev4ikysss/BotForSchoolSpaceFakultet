from .api_module import ApiModule


class Search(ApiModule):
    __slots__ = ()

    def getHints(self,
                 q=None,
                 offset=None,
                 limit=9,
                 filters=None,
                 fields=None,
                 search_global=True):
        return self._get_response(locals())
