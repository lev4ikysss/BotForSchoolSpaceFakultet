from .api_module import ApiModule


class Board(ApiModule):
    __slots__ = ()

    def addTopic(self, group_id, title, text=None, from_group=False, attachments=None):
        return self._get_response(locals())

    def closeTopic(self, group_id, topic_id):
        return self._get_response(locals())

    def createComment(self,
                      group_id,
                      topic_id,
                      message=None,
                      attachments=None,
                      from_group=False,
                      sticker_id=None,
                      guid=None):
        return self._get_response(locals())

    def deleteComment(self, group_id, topic_id, comment_id):
        return self._get_response(locals())

    def deleteTopic(self, group_id, topic_id):
        return self._get_response(locals())

    def editComment(self,
                    group_id,
                    topic_id,
                    comment_id,
                    message=None,
                    attachments=None):
        return self._get_response(locals())

    def editTopic(self, group_id, topic_id, title):
        return self._get_response(locals())

    def fixTopic(self, group_id, topic_id):
        return self._get_response(locals())

    def getComments(self,
                    group_id,
                    topic_id,
                    need_likes=False,
                    start_comment_id=None,
                    offset=None,
                    count=20,
                    extended=False,
                    sort=None):
        return self._get_response(locals())

    def getTopics(self,
                  group_id,
                  topic_ids=None,
                  order=None,
                  offset=None,
                  count=40,
                  extended=False,
                  preview=False,
                  preview_length=90):
        return self._get_response(locals())

    def openTopic(self, group_id, topic_id):
        return self._get_response(locals())

    def restoreComment(self, group_id, topic_id, comment_id):
        return self._get_response(locals())

    def unfixTopic(self, group_id, topic_id):
        return self._get_response(locals())
