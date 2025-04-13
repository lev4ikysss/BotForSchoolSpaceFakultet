from .api_module import ApiModule


class Groups(ApiModule):
    __slots__ = ()

    def addAddress(self,
                   group_id,
                   title,
                   address,
                   country_id,
                   city_id,
                   latitude,
                   longitude,
                   additional_address=None,
                   metro_id=None,
                   phone=None,
                   work_info_status='no_information',
                   timetable=None,
                   is_main_address=None):
        timetable = ApiModule.seralize(timetable)
        return self._get_response(locals())

    def addCallbackServer(self, group_id, url, title, secret_key=None):
        return self._get_response(locals())

    def addLink(self, group_id, link, text=None):
        return self._get_response(locals())

    def approveRequest(self, group_id, user_id):
        return self._get_response(locals())

    def ban(self,
            group_id,
            owner_id=None,
            end_date=None,
            reason=0,
            comment=None,
            comment_visible=0):
        return self._get_response(locals())

    def create(self,
               title,
               description=None,
               _type='group',
               public_category=None,
               subtype=None):
        return self._get_response(locals())

    def deleteAddress(self, group_id, address_id):
        return self._get_response(locals())

    def deleteCallbackServer(self, group_id, server_id):
        return self._get_response(locals())

    def deleteLink(self, group_id, link_id):
        return self._get_response(locals())

    def disableOnline(self, group_id):
        return self._get_response(locals())

    def edit(self,
             group_id,
             title=None,
             description=None,
             screen_name=None,
             access=None,
             website=None,
             subject=None,
             email=None,
             phone=None,
             res=None,
             event_start_date=None,
             event_finish_date=None,
             event_group_id=None,
             public_category=None,
             public_date=None,
             wall=None,
             topics=None,
             photos=None,
             video=None,
             audio=None,
             likes=None,
             events=None,
             places=None,
             contacts=None,
             docs=None,
             wiki=None,
             messages=None,
             articles=None,
             addresses=None,
             age_limits=None,
             market=None,
             market_comments=None,
             market_country=None,
             market_city=None,
             market_currency=None,
             market_contacts=None,
             market_wiki=None,
             obscene_filter=None,
             obscene_words=None,
             main_section=None,
             secondary_section=None,
             country=None,
             city=None):
        return self._get_response(locals())

    def editAddress(self,
                    group_id,
                    address_id,
                    title=None,
                    address=None,
                    additional_address=None,
                    country_id=None,
                    city_id=None,
                    metro_id=None,
                    latitude=None,
                    longitude=None,
                    phone=None,
                    work_info_status=None,
                    timetable=None,
                    is_main_address=None):
        timetable = ApiModule.seralize(timetable)
        return self._get_response(locals())

    def editCallbackServer(self,
                           group_id,
                           server_id,
                           url,
                           title,
                           secret_key=None):
        return self._get_response(locals())

    def editLink(self, group_id, link_id, text=None):
        return self._get_response(locals())

    def editManager(self,
                    group_id,
                    user_id,
                    role=None,
                    is_contact=None,
                    contact_position=None,
                    contact_phone=None,
                    contact_email=None):
        return self._get_response(locals())

    def enableOnline(self, group_id):
        return self._get_response(locals())

    def get(self,
            user_id=None,
            extended=False,
            _filter=None,
            fields=None,
            offset=None,
            count=None):
        return self._get_response(locals())

    def getAddress(self,
                   group_id,
                   address_ids=None,
                   latitude=None,
                   longitude=None,
                   offset=None,
                   count=10,
                   fields=None):
        return self._get_response(locals())

    def getBanned(self,
                  group_id,
                  offset=None,
                  count=20,
                  fields=None,
                  owner_id=None):
        return self._get_response(locals())

    def getById(self, group_ids=None, group_id=None, fields=None):
        return self._get_response(locals())

    def getCallbackConfirmationCode(self, group_id):
        return self._get_response(locals())

    def getCallbackServers(self, group_id, server_ids=None):
        return self._get_response(locals())

    def getCallbackSettings(self, group_id, server_id=None):
        return self._get_response(locals())

    def getCatalog(self, category_id=None, subcategory_id=None):
        return self._get_response(locals())

    def getCatalogInfo(self, extended=0, subcategories=False):
        return self._get_response(locals())

    def getInvitedUsers(self,
                        group_id,
                        offset=None,
                        count=20,
                        fields=None,
                        name_case='nom'):
        return self._get_response(locals())

    def getInvites(self, offset=None, count=20, extended=0):
        return self._get_response(locals())

    def getLongPollServer(self, group_id):
        return self._get_response(locals())

    def getLongPollSettings(self, group_id):
        return self._get_response(locals())

    def getMembers(self,
                   group_id=None,
                   sort='id_ask',
                   offset=None,
                   count=1000,
                   fields=None,
                   _filter=None):
        return self._get_response(locals())

    def getOnlineStatus(self, group_id):
        return self._get_response(locals())

    def getRequests(self,
                    group_id,
                    offset=0,
                    count=20,
                    fields=None):
        return self._get_response(locals())

    def getSettings(self, group_id):
        return self._get_response(locals())

    def getTokenPermissions(self):
        return self._get_response(locals())

    def invite(self, group_id, user_id):
        return self._get_response(locals())

    def isMember(self,
                 group_id,
                 user_id=None,
                 user_ids=None,
                 extended=False):
        return self._get_response(locals())

    def join(self, group_id=None, not_sure=0):
        return self._get_response(locals())

    def leave(self, group_id):
        return self._get_response(locals())

    def removeUser(self, group_id, user_id):
        return self._get_response(locals())

    def reorderLink(self, group_id, link_id, after=None):
        return self._get_response(locals())

    def search(self,
               q,
               _type=None,
               country_id=None,
               city_id=None,
               future=None,
               market=None,
               sort=None,
               offset=0,
               count=20):
        return self._get_response(locals())

    def setCallbackSettings(self,
                            group_id,
                            server_id=None,
                            api_version=None,
                            message_new=None,
                            message_reply=None,
                            message_allow=None,
                            message_edit=None,
                            message_deny=None,
                            message_typing_state=None,
                            photo_new=None,
                            audio_new=None,
                            video_new=None,
                            wall_reply_new=None,
                            wall_reply_edit=None,
                            wall_reply_restore=None,
                            wall_reply_delete=None,
                            wall_post_new=None,
                            wall_repost=None,
                            board_post_new=None,
                            board_post_edit=None,
                            board_post_delete=None,
                            board_post_restore=None,
                            photo_comment_new=None,
                            photo_comment_edit=None,
                            photo_comment_delete=None,
                            photo_comment_restore=None,
                            video_comment_new=None,
                            video_comment_edit=None,
                            video_comment_delete=None,
                            video_comment_restore=None,
                            market_comment_new=None,
                            market_comment_edit=None,
                            market_comment_delete=None,
                            market_comment_restore=None,
                            poll_vote_new=None,
                            group_join=None,
                            group_leave=None,
                            group_change_settings=None,
                            group_change_photo=None,
                            group_officers_edit=None,
                            user_block=None,
                            user_unblock=None,
                            lead_forms_new=None):
        return self._get_response(locals())

    def setLongPollSettings(self,
                            group_id,
                            enabled=None,
                            api_version=None,
                            message_new=None,
                            message_reply=None,
                            message_allow=None,
                            message_edit=None,
                            message_deny=None,
                            message_typing_state=None,
                            photo_new=None,
                            audio_new=None,
                            video_new=None,
                            wall_reply_new=None,
                            wall_reply_edit=None,
                            wall_reply_restore=None,
                            wall_reply_delete=None,
                            wall_post_new=None,
                            wall_repost=None,
                            board_post_new=None,
                            board_post_edit=None,
                            board_post_delete=None,
                            board_post_restore=None,
                            photo_comment_new=None,
                            photo_comment_edit=None,
                            photo_comment_delete=None,
                            photo_comment_restore=None,
                            video_comment_new=None,
                            video_comment_edit=None,
                            video_comment_delete=None,
                            video_comment_restore=None,
                            market_comment_new=None,
                            market_comment_edit=None,
                            market_comment_delete=None,
                            market_comment_restore=None,
                            poll_vote_new=None,
                            group_join=None,
                            group_leave=None,
                            group_change_settings=None,
                            group_change_photo=None,
                            group_officers_edit=None,
                            user_block=None,
                            user_unblock=None):
        return self._get_response(locals())

    def setSettings(self,
                    group_id,
                    messages=None,
                    bots_capabilities=None,
                    bots_start_button=None,
                    bots_add_to_chat=None):
        return self._get_response(locals())

    def unban(self, group_id, owner_id):
        return self._get_response(locals())
