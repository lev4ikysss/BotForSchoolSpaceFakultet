from .api_module import ApiModule


class Market(ApiModule):
    __slots__ = ()

    def add(self,
            owner_id,
            name,
            description,
            category,
            price,
            main_photo_id,
            deleted=None,
            photo_ids=None,
            url=None):
        return self._get_response(locals())

    def addAlbum(self,
                 owner_id,
                 title,
                 photo_id=None,
                 main_album=None):
        return self._get_response(locals())

    def addToAlbum(self,
                   owner_id,
                   item_id,
                   album_ids):
        return self._get_response(locals())

    def createComment(self,
                      owner_id,
                      item_id,
                      message=None,
                      attachments=None,
                      from_group=False,
                      reply_to_comment=None,
                      sticker_id=None,
                      guid=None):
        return self._get_response(locals())

    def delete(self, owner_id, item_id):
        return self._get_response(locals())

    def deleteAlbum(self, owner_id, album_id):
        return self._get_response(locals())

    def deleteComment(self, owner_id, comment_id):
        return self._get_response(locals())

    def edit(self,
             owner_id,
             item_id,
             name=None,
             description=None,
             category=None,
             price=None,
             deleted=None,
             main_photo_id=None,
             photo_ids=None,
             url=None):
        return self._get_response(locals())

    def editAlbum(self,
                  owner_id,
                  album_id,
                  title,
                  photo_id=None,
                  main_album=None):
        return self._get_response(locals())

    def editComment(self,
                    owner_id,
                    comment_id,
                    message=None,
                    attachments=None):
        return self._get_response(locals())

    def get(self,
            owner_id,
            album_id=None,
            count=100,
            offset=None,
            extended=False):
        return self._get_response(locals())

    def getAlbumById(self, owner_id, album_id):
        return self._get_response(locals())

    def getAlbums(self, owner_id, offset=None, count=50):
        return self._get_response(locals())

    def getById(self, item_ids, extended=False):
        return self._get_response(locals())

    def getCategories(self, count=10, offset=None):
        return self._get_response(locals())

    def getComments(self,
                    owner_id,
                    item_id,
                    need_likes=None,
                    start_comment_id=None,
                    offset=None,
                    count=20,
                    sort='asc',
                    extended=None,
                    fields=None):
        return self._get_response(locals())

    def removeFromAlbum(self, owner_id, item_id, album_ids):
        return self._get_response(locals())

    def reorderAlbums(self, owner_id, album_id, before=None, after=None):
        return self._get_response(locals())

    def reorderItems(self,
                     owner_id,
                     item_id,
                     album_id=None,
                     before=None,
                     after=None):
        return self._get_response(locals())

    def report(self,
               owner_id,
               item_id,
               reason):
        return self._get_response(locals())

    def reportComment(self, owner_id, comment_id, reason):
        return self._get_response(locals())

    def restore(self, owner_id, item_id):
        return self._get_response(locals())

    def restoreComment(self, owner_id, comment_id):
        return self._get_response(locals())

    def search(self,
               owner_id,
               album_id=0,
               q=None,
               price_from=None,
               price_to=None,
               tags=None,
               sort=False,
               rev=True,
               offset=None,
               cunt=20,
               extended=False,
               status=False):
        return self._get_response(locals())
