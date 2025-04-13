from .api_module import ApiModule


class Docs(ApiModule):
    __slots__ = ()

    def add(self, owner_id, doc_id, access_key=None):
        return self._get_response(locals())

    def delete(self, owner_id, doc_id):
        return self._get_response(locals())

    def edit(self, owner_id, doc_id, title=None, tags=None):
        return self._get_response(locals())

    def get(self, count=None, offset=None, _type=None, owner_id=None):
        return self._get_response(locals())

    def getById(self, docs):
        return self._get_response(locals())

    def getMessagesUploadServer(self, _type='doc', peer_id=None):
        return self._get_response(locals())

    def getTypes(self, owner_id):
        return self._get_response(locals())

    def getUploadServer(self, group_id=None):
        return self._get_response(locals())

    def getWallUploadServer(self, group_id=None):
        return self._get_response(locals())

    def save(self, file, title=None, tags=None):
        return self._get_response(locals())

    def search(self, q, search_own=None, count=None, offset=None):
        return self._get_response(locals())
