from .api_module import ApiModule


class Messages(ApiModule):
    __slots__ = ()

    def addChatUser(self, chat_id, user_id):
        return self._get_response(locals())

    def allowMessagesFromGroup(self, group_id, key=None):
        return self._get_response(locals())

    def createChat(self, user_ids=None, title=None):
        return self._get_response(locals())

    def delete(self, message_ids=None, spam=None, group_id=None, delete_for_all=False):
        return self._get_response(locals())

    def deleteChatPhoto(self, chat_id, group_id=None):
        return self._get_response(locals())

    def deleteConversation(self, user_id=None, peer_id=None, group_id=None):
        return self._get_response(locals())

    def denyMessagesGroup(self, group_id):
        return self._get_response(locals())

    def edit(self,
             peer_id,
             message_id,
             message=None,
             lat=None,
             long=None,
             attachment=None,
             keep_forward_messages=None,
             keep_snippets=None,
             group_id=None,
             dont_parse_links=False):
        return self._get_response(locals())

    def editChat(self, chat_id, title):
        return self._get_response(locals())

    def getByConversationMessageId(self, peer_id, conversation_message_ids, extended=None, fields=None, group_id=None):
        return self._get_response(locals())

    def getById(self,
                message_ids,
                preview_length=0,
                extended=None,
                fields=None,
                group_id=None):
        return self._get_response(locals())

    def getChat(self,
                chat_id=None,
                chat_ids=None,
                fields=None,
                name_case='nom'):
        return self._get_response(locals())

    def getChatPreview(self, peer_id=None, link=None, fields=None):
        return self._get_response(locals())

    def getConversationMembers(self, peer_id, fields=None, group_id=None):
        return self._get_response(locals())

    def getConversations(self,
                         offset=0,
                         count=20,
                         _filter='all',
                         extended=None,
                         start_message_id=None,
                         fields=None,
                         group_id=None):
        return self._get_response(locals())

    def getConversationById(self,
                            peer_ids,
                            extended=None,
                            fields=None,
                            group_id=None):
        return self._get_response(locals())

    def getHistory(self,
                   offset=None,
                   count=20,
                   user_id=None,
                   peer_id=None,
                   start_message_id=None,
                   rev=False,
                   extended=False,
                   fields=None,
                   group_id=None):
        return self._get_response(locals())

    def getHistoryAttachments(self,
                              peer_id,
                              media_type='photo',
                              start_from=None,
                              count=30,
                              photo_sizes=None,
                              fields=None,
                              group_id=None,
                              preserve_order=None,
                              max_forwards_level=45):
        return self._get_response(locals())

    def getImportantMessages(self,
                             count=20,
                             offset=None,
                             start_message_id=None,
                             preview_length=None,
                             fields=None,
                             extended=None,
                             group_id=None):
        return self._get_response(locals())

    def getInviteLink(self, peer_id, reset=False, group_id=None):
        return self._get_response(locals())

    def getLastActivity(self, user_id):
        return self._get_response(locals())

    def getLongPollHistory(self,
                           ts=None,
                           pts=None,
                           preview_length=None,
                           onlines=None,
                           fields=None,
                           events_limit=1000,
                           msgs_limit=200,
                           max_msg_id=None,
                           group_id=None,
                           lp_version=None,
                           last_n=0,
                           credentials=None):
        return self._get_response(locals())

    def getLongPollServer(self, need_pts=None, group_id=None, lp_version=0):
        return self._get_response(locals())

    def isMessagesFromGroupAllowed(self, group_id, user_id):
        return self._get_response(locals())

    def joinChatByInviteLink(self, link):
        return self._get_response(locals())

    def markAsAnsweredConversation(self, peer_id, answered=1, group_id=None):
        return self._get_response(locals())

    def markAsImportant(self, message_ids=None, important=None):
        return self._get_response(locals())

    def markAsImportantConversation(self, peer_id, important=1, group_id=None):
        return self._get_response(locals())

    def markAsRead(self,
                   message_ids=None,
                   peer_id=None,
                   start_message_id=None,
                   group_id=None):
        return self._get_response(locals())

    def pin(self, peer_id, message_id=None):
        return self._get_response(locals())

    def removeChatUser(self, chat_id, user_id=None, member_id=None):
        return self._get_response(locals())

    def restore(self, message_id, group_id=None):
        return self._get_response(locals())

    def search(self,
               q=None,
               peer_id=None,
               date=None,
               preview_length=0,
               offset=0,
               count=20,
               extended=None,
               fields=None,
               group_id=None):
        return self._get_response(locals())

    def searchConversation(self, q=None, count=20, extended=None, fields=None, group_id=None):
        return self._get_response(locals())

    def send(self,
             user_id=None,
             random_id=None,
             peer_id=None,
             domain=None,
             chat_id=None,
             user_ids=None,
             message=None,
             lat=None,
             long=None,
             attachment=None,
             eply_to=None,
             forward_messages=None,
             sticker_id=None,
             group_id=None,
             keyboard=None,
             payload=None,
             dont_parse_links=False,
             disable_mentions=False):
        return self._get_response(locals())

    def setActivity(self, user_id=None, _type=None, peer_id=None, group_id=None):
        return self._get_response(locals())

    def setChatPhoto(self, file):
        return self._get_response(locals())

    def unpin(self, peer_id, group_id=None):
        return self._get_response(locals())
