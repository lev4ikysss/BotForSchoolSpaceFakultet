from .api_module import ApiModule


class Wall(ApiModule):
    __slots__ = ()

    def closeComments(self, owner_id, post_id):
        return self._get_response(locals())

    def createComment(self,
                      post_id,
                      owner_id=None,
                      from_group=False,
                      message=None,
                      reply_to_comment=None,
                      attachments=None,
                      sticker_id=None,
                      guid=None):
        return self._get_response(locals())

    def delete(self, owner_id=None, post_id=None):
        return self._get_response(locals())

    def deleteComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def edit(self,
             post_id,
             owner_id=None,
             friends_only=None,
             message=None,
             attachments=None,
             services=None,
             signed=None,
             publish_date=None,
             lat=None,
             long=None,
             place_id=None,
             mark_as_ds=None,
             close_comments=None,
             poster_bkg_id=None,
             poster_bkg_owner_id=None,
             poster_bkg_access_hash=None):
        return self._get_response(locals())

    def editAdsStealth(self,
                       post_id,
                       owner_id=None,
                       message=None,
                       attachments=None,
                       signed=None,
                       lat=None,
                       long=None,
                       place_id=None,
                       link_button=None,
                       link_title=None,
                       link_image=None,
                       link_video=None):
        return self._get_response(locals())

    def editComment(self,
                    comment_id,
                    owner_id=None,
                    message=None,
                    attachments=None):
        return self._get_response(locals())

    def get(self,
            owner_id=None,
            domain=None,
            offset=None,
            count=None,
            _filter=None,
            extended=False,
            fields=None):
        return self._get_response(locals())

    def getById(self,
                posts,
                extended=False,
                copy_history_depth=2,
                fields=None):
        return self._get_response(locals())

    def getComment(self, comment_id, owner_id=None, extended=0, fields=None):
        return self._get_response(locals())

    def getComments(self,
                    owner_id=None,
                    post_id=None,
                    need_likes=None,
                    start_comment_id=None,
                    offset=None,
                    count=10,
                    sort=None,
                    preview_length=None,
                    extended=False,
                    fields=None,
                    comment_id=None,
                    thread_items_count=0):
        return self._get_response(locals())

    def getReposts(self,
                   owner_id=None,
                   post_id=None,
                   offset=None,
                   count=20):
        return self._get_response(locals())

    def openComments(self, owner_id, post_id):
        return self._get_response(locals())

    def pin(self, post_id, owner_id=None):
        return self._get_response(locals())

    def post(self,
             owner_id=None,
             friends_only=False,
             from_group=False,
             message=None,
             attachments=None,
             services=None,
             signed=False,
             publish_date=None,
             lat=None,
             long=None,
             place_id=None,
             post_id=None,
             guid=None,
             mark_as_ads=False,
             close_comment=None,
             mute_notifications=None):
        return self._get_response(locals())

    def postAdsStealth(self,
                       owner_id,
                       message=None,
                       attachments=None,
                       signed=False,
                       lat=None,
                       long=None,
                       place_id=None,
                       guid=None,
                       lnk_button=None,
                       link_title=None,
                       link_image=None,
                       link_video=None):
        return self._get_response(locals())

    def reportComment(self, owner_id, comment_id, reason=None):
        return self._get_response(locals())

    def reportPost(self, owner_id, post_id, reason=None):
        return self._get_response(locals())

    def repost(self, _object, message=None, group_id=None, mark_as_ads=False, mute_notifications=None):
        return self._get_response(locals())

    def restore(self, owner_id=None, post_id=None):
        return self._get_response(locals())

    def restoreComment(self, comment_id, owner_id=None):
        return self._get_response(locals())

    def search(self,
               owner_id=None,
               domain=None,
               query=None,
               owners_only=None,
               count=20,
               offset=0,
               extended=False,
               fields=None):
        return self._get_response(locals())

    def unpin(self, post_id, owner_id=None):
        return self._get_response(locals())
