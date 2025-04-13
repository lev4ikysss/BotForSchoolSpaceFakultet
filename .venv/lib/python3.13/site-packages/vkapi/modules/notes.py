from .api_module import ApiModule


class Notes(ApiModule):
    __slots__ = ()

    def add(self, title, text, privacy_view='all', privacy_comment='all'):
        return self._get_response(locals())

    def createComment(self, note_id, message, owner_id=None, reply_to=None, guid=None):
        return self._get_response(locals())

    def delete(self, note_id):
        return self._get_response(locals())

    def deleteComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def edit(self, note_id, title, text, privacy_view='all', privacy_comment='all'):
        return self._get_response(locals())

    def editComment(self, comment_id, owner_id=None, message=None):
        return self._get_response(locals())

    def get(self, note_ids=None, user_id=None, offset=0, count=20, sort=False):
        return self._get_response(locals())

    def getById(self, note_id, owner_id=None, need_wiki=False):
        return self._get_response(locals())

    def getComments(self, note_id, owner_id=None, sort=False, offset=0, count=20):
        return self._get_response(locals())

    def restoreComment(self, comment_id, owner_id=None):
        return self._get_response(locals())
