from .api_module import ApiModule


class Friends(ApiModule):
    __slots__ = ()

    def add(self, user_id=None, text=None, follow=None):
        return self._get_response(locals())

    def addList(self, name, user_ids=None):
        return self._get_response(locals())

    def areFriends(self, user_ids, need_sign=None):
        return self._get_response(locals())

    def delete(self, user_id=None):
        return self._get_response(locals())

    def deleteAllRequests(self):
        return self._get_response(locals())

    def deleteList(self, list_id):
        return self._get_response(locals())

    def edit(self, user_id, list_ids=None):
        return self._get_response(locals())

    def editList(self, list_id, name=None, user_ids=None, add_user_ids=None, delete_user_ids=None):
        return self._get_response(locals())

    def get(self,
            user_id=None,
            order=None,
            list_id=None,
            count=5000,
            offset=None,
            fields=None,
            name_case='nom',
            ref=None):
        return self._get_response(locals())

    def getAppUsers(self):
        return self._get_response(locals())

    def getByPhones(self, phones=None, fields=None):
        return self._get_response(locals())

    def getList(self, user_id=None, return_system=None):
        return self._get_response(locals())

    def getMutual(self,
                  source_id=None,
                  target_uid=None,
                  target_uids=None,
                  order=None,
                  count=None,
                  offset=None):
        return self._get_response(locals())

    def getOnline(self,
                  user_id=None,
                  list_id=None,
                  online_mobile=False,
                  order=None,
                  count=None,
                  offset=None):
        return self._get_response(locals())

    def getRecent(self, count=100):
        return self._get_response(locals())

    def getRequests(self,
                    offset=None,
                    count=100,
                    extended=None,
                    need_mutual=None,
                    out=False,
                    sort=None,
                    need_viewed=False,
                    suggested=False,
                    ref=None,
                    fields=None):
        return self._get_response(locals())

    def getSuggestions(self,
                       _filter=None,
                       count=500,
                       offset=None,
                       fields=None,
                       name_case='nom'):
        return self._get_response(locals())

    def search(self,
               user_id,
               q=None,
               fields=None,
               name_case='nom',
               offset=None,
               count=20):
        return self._get_response(locals())
