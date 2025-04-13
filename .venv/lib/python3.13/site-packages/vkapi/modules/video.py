from .api_module import ApiModule


class Video(ApiModule):
    __slots__ = ()

    def add(self, video_id, owner_id, target_id=None):
        return self._get_response(locals())

    def addAlbum(self, group_id=None, title=None, privacy=None):
        return self._get_response(locals())

    def addToAlbum(self, owner_id, video_id, target_id=None, album_id=None, album_ids=None):
        return self._get_response(locals())

    def createComment(self,
                      video_id,
                      owner_id=None,
                      message=None,
                      attachments=None,
                      from_group=False,
                      reply_to_comment=None,
                      sticker_id=None,
                      guid=None):
        return self._get_response(locals())

    def delete(self, video_id, owner_id=None, target_id=None):
        return self._get_response(locals())

    def deleteAlbum(self, album_id, group_id=None):
        return self._get_response(locals())

    def deleteComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def edit(self,
             video_id,
             owner_id=None,
             name=None,
             desc=None,
             privacy_view=None,
             privacy_comment=None,
             no_comments=None,
             repeat=None):
        return self._get_response(locals())

    def editAlbum(self, album_id, title, group_id=None, privacy=None):
        return self._get_response(locals())

    def editComment(self, comment_id, owner_id=None, message=None, attachments=None):
        return self._get_response(locals())

    def get(self,
            owner_id=None,
            videos=None,
            album_id=None,
            count=100,
            offset=None,
            extended=None):
        return self._get_response(locals())

    def getAlbumById(self, album_id, owner_id=None):
        return self._get_response(locals())

    def getAlbums(self, owner_id=None, offset=0, count=50, extended=False, need_system=False):
        return self._get_response(locals())

    def getAlbumsByVideo(self, owner_id, video_id, target_id=None, extended=False):
        return self._get_response(locals())

    def getComments(self,
                    video_id,
                    owner_id=None,
                    need_likes=False,
                    start_comment_id=None,
                    offset=0,
                    count=20,
                    sort=None,
                    extended=False,
                    fields=None):
        return self._get_response(locals())

    def removeFromAlbum(self, owner_id, video_id, target_id=None, album_id=None, album_ids=None):
        return self._get_response(locals())

    def reorderAlbums(self, album_id, owner_id=None, before=None, after=None):
        return self._get_response(locals())

    def reorderVideos(self,
                      video_id,
                      owner_id,
                      target_id=None,
                      album_id=None,
                      before_owner_id=None,
                      before_video_id=None,
                      after_owner_id=None,
                      after_video_id=None):
        return self._get_response(locals())

    def report(self, owner_id, video_id, reason=None, comment=None, search_query=None):
        return self._get_response(locals())

    def reportComment(self, owner_id, comment_id, reason=None):
        return self._get_response(locals())

    def restore(self, video_id, owner_id=None):
        return self._get_response(locals())

    def restoreComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def save(self,
             name=None,
             description=None,
             is_private=False,
             wallpost=None,
             link=None,
             group_id=None,
             album_id=None,
             privacy_view=None,
             privacy_comment=None,
             no_comments=None,
             repeat=None,
             compression=None):
        return self._get_response(locals())

    def search(self,
               q=None,
               sort=None,
               hd=None,
               adult=None,
               filters=None,
               search_own=False,
               offset=None,
               longer=None,
               shorter=None,
               count=20,
               extended=False):
        return self._get_response(locals())
