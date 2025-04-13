from .api_module import ApiModule


class Fave(ApiModule):
    __slots__ = ()

    def addArticle(self, url, ref=None, track_code=None, source=None):
        return self._get_response(locals())

    def addLink(self, link):
        return self._get_response(locals())

    def addPage(self, user_id=None, group_id=None):
        return self._get_response(locals())

    def addPost(self, owner_id, _id, access_key=None, ref=None, track_code=None, source=None):
        return self._get_response(locals())

    def addProduct(self, owner_id, _id, access_key=None, ref=None, source=None):
        return self._get_response(locals())

    def addTag(self, name):
        return self._get_response(locals())

    def addVideo(self, owner_id, _id, access_key=None, ref=None):
        return self._get_response(locals())

    def editTag(self, _id, name):
        return self._get_response(locals())

    def get(self, extended=0, item_type=None, tag_id=None, offset=None, count=50, fields=None, is_from_snackbar=None):
        return self._get_response(locals())

    def getPages(self, offset=None, count=50, _type=None, fields=None, tag_id=None):
        return self._get_response(locals())

    def getTags(self):
        return self._get_response(locals())

    def markSeen(self):
        return self._get_response(locals())

    def removeArticle(self, owner_id, article_id, ref=None):
        return self._get_response(locals())

    def removeLink(self, link_id):
        return self._get_response(locals())

    def removePage(self, user_id=None, group_id=None):
        return self._get_response(locals())

    def removePost(self, owner_id, _id):
        return self._get_response(locals())

    def removeProduct(self, owner_id, _id):
        return self._get_response(locals())

    def removeTag(self, _id):
        return self._get_response(locals())

    def removeVideo(self, owner_id, _id):
        return self._get_response(locals())

    def reorderTags(self, ids):
        return self._get_response(locals())

    def setPageTags(self, user_id=None, group_id=None, tag_ids=None, ref=None):
        return self._get_response(locals())

    def setTags(self,
                item_type=None,
                item_owner_id=None,
                item_id=None,
                tag_ids=None,
                link_id=None,
                link_url=None,
                ref=None):
        return self._get_response(locals())

    def trackPageInteraction(self, user_id=None, group_id=None):
        return self._get_response(locals())
