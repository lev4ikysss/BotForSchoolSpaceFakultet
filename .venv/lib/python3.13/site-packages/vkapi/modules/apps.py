from .api_module import ApiModule


class Apps(ApiModule):
    __slots__ = ()

    def deleteAppRequests(self):
        return self._get_response(locals())

    def get(self,
            app_id=None,
            app_ids=None,
            platform='web',
            extended=False,
            return_friends=False,
            fields=None,
            name_case='nom'):
        return self._get_response(locals())

    def getCatalog(self,
                   sort=None,
                   offset=None,
                   count=None,
                   platform='web',
                   extended=None,
                   return_friends=False,
                   fields=None,
                   name_case='nom',
                   q=None,
                   genre_id=None,
                   _filter=None):
        return self._get_response(locals())

    def getFriendsList(self, extended=False, count=20, offset=0, _type='invite', fields=None):
        return self._get_response(locals())

    def getLeaderboard(self, _type, _global=True, extended=False):
        return self._get_response(locals())

    def getScopes(self, _type='user'):
        return self._get_response(locals())

    def getScore(self, user_id):
        return self._get_response(locals())

    def sendRequest(self,
                    user_id,
                    text=None,
                    _type='request',
                    name=None,
                    key=None,
                    separate=False):
        return self._get_response(locals())
