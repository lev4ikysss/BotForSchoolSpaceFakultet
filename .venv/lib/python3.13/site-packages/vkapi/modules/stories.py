from .api_module import ApiModule


class Stories(ApiModule):
    __slots__ = ()

    def banOwner(self, owner_ids):
        return self._get_response(locals())

    def delete(self, story_id, owner_id=None):
        return self._get_response(locals())

    def get(self, owner_id=None, extended=False):
        return self._get_response(locals())

    def getBanned(self, extended=None, fields=None):
        return self._get_response(locals())

    def getById(self, stories, extended=False, fields=None):
        return self._get_response(locals())

    def getPhotoUploadServer(self,
                             add_to_news=None,
                             user_ids=None,
                             reply_to_story=None,
                             link_text=None,
                             link_url=None,
                             group_id=None):
        return self._get_response(locals())

    def getReplies(self, owner_id, story_id, access_key=None, extended=False, fields=None):
        return self._get_response(locals())

    def getStats(self, owner_id, story_id):
        return self._get_response(locals())

    def getVideoUploadServer(self,
                             add_to_news=None,
                             user_ids=None,
                             reply_to_story=None,
                             link_text=None,
                             link_url=None,
                             group_id=None):
        return self._get_response(locals())

    def getViewers(self, story_id, owner_id=None, count=100, offset=0, extended=False):
        return self._get_response(locals())

    def hideAllReplies(self, owner_id, group_id=None):
        return self._get_response(locals())

    def hideReply(self, owner_id, story_id, access_key=None):
        return self._get_response(locals())

    def unbanOwner(self, owners_ids):
        return self._get_response(locals())
