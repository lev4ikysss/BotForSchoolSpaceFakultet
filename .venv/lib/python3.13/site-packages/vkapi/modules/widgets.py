from .api_module import ApiModule


class Widgets(ApiModule):
    __slots__ = ()

    def getComments(self,
                    widget_api_id=None,
                    url=None,
                    page_id=None,
                    order=None,
                    fields=None,
                    offset=0,
                    count=10):
        return self._get_response(locals())

    def getPages(self,
                 widget_api_id=None,
                 order=None,
                 period='week',
                 offset=0,
                 count=10):
        return self._get_response(locals())
