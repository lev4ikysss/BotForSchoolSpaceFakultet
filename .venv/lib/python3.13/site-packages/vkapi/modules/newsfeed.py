from .api_module import ApiModule


class Newsfeed(ApiModule):
    __slots__ = ()

    def addBan(self, user_ids=None, group_ids=None):
        return self._get_response(locals())

    def deleteBan(self, user_ids=None, group_ids=None):
        return self._get_response(locals())

    def deleteList(self, list_id):
        return self._get_response(locals())

    def get(self,
            filters=None,
            return_banned=None,
            start_time=None,
            end_time=None,
            max_photos=5,
            source_ids=None,
            start_from=None,
            count=50,
            fields=None,
            section=None):
        return self._get_response(locals())

    def getBanned(self, extended=None, fields=None, name_case='nom'):
        return self._get_response(locals())

    def getComments(self,
                    count=30,
                    filters=None,
                    reposts=None,
                    start_time=None,
                    end_time=None,
                    list_comments_count=0,
                    start_from=None,
                    fields=None):
        return self._get_response(locals())

    def getList(self, list_ids=None, extended=False):
        return self._get_response(locals())

    def getMentions(self,
                    owner_id=None,
                    start_time=None,
                    end_time=None,
                    offset=0,
                    count=20):
        return self._get_response(locals())

    def getRecommended(self,
                       start_time=None,
                       end_time=None,
                       max_photos=5,
                       start_from=None,
                       count=50,
                       fields=None):
        return self._get_response(locals())

    def getSuggestedSources(self, offset=None, count=20, shuffle=None, fields=None):
        return self._get_response(locals())

    def ignoreItem(self, _type, owner_id, item_id):
        return self._get_response(locals())

    def saveList(self,
                 title,
                 list_id=None,
                 source_ids=None,
                 no_reposts=None):
        return self._get_response(locals())

    def search(self,
               q=None,
               extended=False,
               count=30,
               latitude=None,
               longitude=None,
               start_time=None,
               end_time=None,
               start_from=None,
               fields=None):
        return self._get_response(locals())

    def unignoreItem(self, _type, owner_id, item_id):
        return self._get_response(locals())

    def unsubscribe(self, _type, item_id, owner_id=None):
        return self._get_response(locals())
