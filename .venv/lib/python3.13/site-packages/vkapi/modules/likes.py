from .api_module import ApiModule


class Likes(ApiModule):
    __slots__ = ()

    def add(self, _type, item_id, owner_id=None, access_key=None):
        return self._get_response(locals())

    def delete(self, _type, item_id, owner_id=None):
        return self._get_response(locals())

    def getList(self,
                _type,
                owner_id=None,
                item_id=None,
                page_url=None,
                _filter=None,
                friends_only=False,
                extended=False,
                offset=0,
                count=100,
                skip_own=None):
        return self._get_response(locals())

    def isLiked(self,
                _type,
                item_id,
                user_id=None,
                owner_id=None):
        return self._get_response(locals())
