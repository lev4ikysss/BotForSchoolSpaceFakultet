from .api_module import ApiModule


class Photos(ApiModule):
    __slots__ = ()

    def confirmTag(self, photo_id, tag_id, owner_id=None):
        return self._get_response(locals())

    def copy(self, owner_id, photo_id, access_key=None):
        return self._get_response(locals())

    def createAlbum(self,
                    title,
                    group_id=None,
                    description=None,
                    privacy_view='all',
                    privacy_comment='all',
                    upload_by_admins_only=None,
                    comments_disabled=None):
        return self._get_response(locals())

    def createComment(self,
                      photo_id,
                      owner_id=None,
                      message=None,
                      attachments=None,
                      from_group=False,
                      reply_to_comment=None,
                      sticker_id=None,
                      access_key=None,
                      guid=None):
        return self._get_response(locals())

    def delete(self, photo_id, owner_id=None):
        return self._get_response(locals())

    def deleteAlbum(self, album_id, group_id=None):
        return self._get_response(locals())

    def deleteComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def edit(self,
             photo_id,
             owner_id=None,
             caption=None,
             latitude=None,
             longitude=None,
             place_str=None,
             foursquere_id=None,
             delete_place=None):
        return self._get_response(locals())

    def editAlbum(self,
                  album_id,
                  title=None,
                  description=None,
                  owner_id=None,
                  privacy_view=None,
                  privacy_comment=None,
                  upload_by_admins_only=None,
                  comments_disabled=None):
        return self._get_response(locals())

    def editComment(self, comment_id, owner_id=None, message=None, attachments=None):
        return self._get_response(locals())

    def get(self,
            owner_id=None,
            album_id=None,
            photo_ids=None,
            rev=None,
            extended=False,
            feed_type=None,
            feed=None,
            photo_sizes=False,
            offset=None,
            count=50):
        return self._get_response(locals())

    def getAlbums(self,
                  owner_id=None,
                  album_ids=None,
                  offset=None,
                  count=None,
                  need_system=None,
                  photo_sizes=None):
        return self._get_response(locals())

    def getAlbumsCount(self, user_id=None, group_id=None):
        return self._get_response(locals())

    def getAll(self,
               owner_id=None,
               extended=None,
               offset=0,
               count=20,
               photo_sizes=None,
               no_service_albums=False,
               need_hidden=None,
               skip_hidden=None):
        return self._get_response(locals())

    def getAllComments(self,
                       owner_id=None,
                       album_id=None,
                       need_likes=None,
                       offset=0,
                       count=20):
        return self._get_response(locals())

    def getById(self, photos, extended=None, photo_sizes=None):
        return self._get_response(locals())

    def getChatUploadServer(self, chat_id, crop_x=None, crop_y=None, crop_width=None):
        return self._get_response(locals())

    def getComments(self,
                    photo_id,
                    owner_id=None,
                    need_likes=False,
                    start_comment_id=None,
                    offset=0,
                    count=20,
                    sort=None,
                    access_key=None,
                    extended=False,
                    fields=None):
        return self._get_response(locals())

    def getMarketAlbumUploadServer(self, group_id):
        return self._get_response(locals())

    def getMarketUploadServer(self, group_id, main_photo=None, crop_x=None, crop_y=None, rop_width=None):
        return self._get_response(locals())

    def getMessagesUploadServer(self, peer_id=None):
        return self._get_response(locals())

    def getNewTags(self, offset=None, count=20):
        return self._get_response(locals())

    def getOwnerCoverPhotoUploadServer(self, group_id, crop_x=0, crop_y=0, crop_x2=795, crop_y2=200):
        return self._get_response(locals())

    def getOwnerPhotoUploadServer(self, owner_id=None):
        return self._get_response(locals())

    def getTags(self, photo_id, owner_id=None, access_key=None):
        return self._get_response(locals())

    def getUploadServer(self, album_id=None, group_id=None):
        return self._get_response(locals())

    def getUserPhotos(self, user_id=None, offset=0, count=20, extended=None, sort=None):
        return self._get_response(locals())

    def getWallUploadServer(self, group_id=None):
        return self._get_response(locals())

    def makeCover(self, photo_id, owner_id=None, album_id=None):
        return self._get_response(locals())

    def move(self, target_album_id, photo_id, owner_id=None):
        return self._get_response(locals())

    def putTag(self, photo_id, user_id, owner_id=None, x=None, y=None, x2=None, y2=None):
        return self._get_response(locals())

    def removeTag(self, photo_id, tag_id, owner_id=None):
        return self._get_response(locals())

    def reorderAlbums(self, album_id, owner_id=None, before=None, after=None):
        return self._get_response(locals())

    def reorderPhotos(self, photo_id, owner_id=None, before=None, after=None):
        return self._get_response(locals())

    def report(self, owner_id, photo_id, reason=None):
        return self._get_response(locals())

    def reportComment(self, owner_id, comment_id, reason=None):
        return self._get_response(locals())

    def restore(self, photo_id, owner_id=None):
        return self._get_response(locals())

    def restoreComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def save(self,
             album_id=None,
             group_id=None,
             server=None,
             photos_list=None,
             _hash=None,
             latitude=None,
             longitude=None,
             caption=None):
        return self._get_response(locals())

    def saveMarketAlbumPhoto(self, group_id, photo, server, _hash):
        return self._get_response(locals())

    def saveMarketPhoto(self, photo, server, _hash, group_id=None, crop_data=None, crop_hash=None):
        return self._get_response(locals())

    def saveMessagesPhoto(self, photo, server=None, _hash=None):
        return self._get_response(locals())

    def saveOwnerCoverPhoto(self, _hash, photo):
        return self._get_response(locals())

    def saveOwnerPhoto(self, server=None, _hash=None, photo=None):
        return self._get_response(locals())

    def saveWallPhoto(self,
                      photo,
                      user_id=None,
                      group_id=None,
                      server=None,
                      _hash=None,
                      latitude=None,
                      longitude=None,
                      caption=None):
        return self._get_response(locals())

    def search(self,
               q=None,
               lat=None,
               long=None,
               start_time=None,
               end_time=None,
               sort=None,
               offset=None,
               count=100,
               radius=5000):
        return self._get_response(locals())
