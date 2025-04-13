from .api_module import ApiModule


class Pages(ApiModule):
    __slots__ = ()

    def clearCache(self, url):
        return self._get_response(locals())

    def get(self,
            owner_id=None,
            page_id=None,
            _global=None,
            site_preview=None,
            title=None,
            need_source=None,
            need_html=None):
        return self._get_response(locals())

    def getHistory(self, page_id, group_id=None, user_id=None):
        return self._get_response(locals())

    def getTitles(self, group_id=None):
        return self._get_response(locals())

    def getVersion(self, version_id, group_id=None, user_id=None, need_html=None):
        return self._get_response(locals())

    def parseWiki(self, text, group_id=None):
        return self._get_response(locals())

    def save(self, text=None, page_id=None, group_id=None, user_id=None, title=None):
        return self._get_response(locals())

    def saveAccess(self, page_id, group_id=None, user_id=None, view=None, edit=None):
        return self._get_response(locals())
