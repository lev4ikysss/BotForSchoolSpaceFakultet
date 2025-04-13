from .api_module import ApiModule


class Ads(ApiModule):
    __slots__ = ()

    def addOfficeUsers(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def checkLink(self, account_id, link_type, link_url, campaign_id=None):
        return self._get_response(locals())

    def createAds(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def createCampaigns(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def createClients(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def createLookalikeRequest(self, account_id, source_type, client_id=None, retargeting_group_id=None):
        return self._get_response(locals())

    def createTargetGroup(self,
                          account_id,
                          name,
                          client_id=None,
                          lifetime=None,
                          target_pixel_id=None,
                          target_pixel_rules=None):
        target_pixel_rules = ApiModule.seralize(target_pixel_rules)
        return self._get_response(locals())

    def createTargetPixel(self, account_id, name, category_id, client_id=None, domain=None):
        return self._get_response(locals())

    def deleteAds(self, account_id, ids):
        ids = ApiModule.seralize(ids)
        return self._get_response(locals())

    def deleteCampaigns(self, account_id, ids):
        ids = ApiModule.seralize(ids)
        return self._get_response(locals())

    def deleteClients(self, account_id, ids):
        ids = ApiModule.seralize(ids)
        return self._get_response(locals())

    def deleteTargetGroup(self, account_id, target_group_id, client_id=None):
        return self._get_response(locals())

    def getAccounts(self):
        return self._get_response(locals())

    def getAds(self,
               account_id,
               ad_ids=None,
               campaign_ids=None,
               client_id=None,
               include_deleted=None,
               limit=None,
               offset=None):
        campaign_ids = ApiModule.seralize(campaign_ids)
        ad_ids = ApiModule.seralize(ad_ids)
        return self._get_response(locals())

    def getAdsLayout(self,
                     account_id,
                     client_id=None,
                     include_deleted=None,
                     campaign_ids=None,
                     ad_ids=None,
                     limit=None,
                     offset=None):
        campaign_ids = ApiModule.seralize(campaign_ids)
        ad_ids = ApiModule.seralize(ad_ids)
        return self._get_response(locals())

    def getAdsTargeting(self,
                        account_id,
                        client_id=None,
                        include_deleted=None,
                        campaign_ids=None,
                        ad_ids=None,
                        limit=None,
                        offset=None):
        campaign_ids = ApiModule.seralize(campaign_ids)
        ad_ids = ApiModule.seralize(ad_ids)
        return self._get_response(locals())

    def getBudget(self, account_id):
        return self._get_response(locals())

    def getCampaigns(self, account_id, client_id=None, include_deleted=None, campaign_ids=None):
        campaign_ids = ApiModule.seralize(campaign_ids)
        return self._get_response(locals())

    def getCategories(self, lang=None):

        return self._get_response(locals())

    def getClients(self, account_id):
        return self._get_response(locals())

    def getDemographics(self, account_id, ids_type, ids, period, date_from, date_to):
        return self._get_response(locals())

    def getFloodStates(self, account_id):
        return self._get_response(locals())

    def getLookalikeRequest(self,
                            account_id,
                            client_id=None,
                            request_ids=None,
                            offset=0,
                            limit=None,
                            sort_by='id'):
        return self._get_response(locals())

    def getOfficeUsers(self, account_id):
        return self._get_response(locals())

    def getPostsReach(self, account_id, ids_type, ids):
        return self._get_response(locals())

    def getRejectionReason(self, account_id, ad_id):
        return self._get_response(locals())

    def getStatistics(self, account_id, ids_type, ids, period, date_from, date_to):
        return self._get_response(locals())

    def getSuggestions(self, section, ids=None, q=None, country=None, cities=None, lang=None):
        return self._get_response(locals())

    def getTargetGroup(self, account_id, client_id=None, extended=None):
        return self._get_response(locals())

    def getTargetPixels(self, account_id, client_id=None):
        return self._get_response(locals())

    def getTargetingStates(self,
                           account_id,
                           link_url,
                           client_id=None,
                           criteria=None,
                           add_id=None,
                           add_format=None,
                           add_platform=None,
                           add_platform_no_wall=None,
                           add_platform_no_add_network=None,
                           link_domain=None):
        criteria = ApiModule.seralize(criteria)
        return self._get_response(locals())

    def getUploadURL(self, ad_format, icon=None):
        return self._get_response(locals())

    def getVideoUploadURL(self):
        return self._get_response(locals())

    def importTargetContacts(self, account_id, target_group_id, contacts, client_id=None):
        return self._get_response(locals())

    def removeOfficeUsers(self, account_id, ids):
        return self._get_response(locals())

    def removeTargetContacts(self, account_id, target_group_id, contacts, client_id=None):
        return self._get_response(locals())

    def saveLookalikeRequestResult(self, account_id, request_id, level, client_id=None):
        return self._get_response(locals())

    def shareTargetGroup(self, account_id, target_group_id, client_id=None, share_with_client_id=None):
        return self._get_response(locals())

    def updateAds(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def updateCampaigns(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def updateClients(self, account_id, data):
        data = ApiModule.seralize(data)
        return self._get_response(locals())

    def updateTargetGroup(self,
                          account_id,
                          target_group_id,
                          name,
                          client_id=None,
                          domain=None,
                          lifetime=None,
                          target_pixel_id=None,
                          target_pixel_rules=None):
        target_pixel_rules = ApiModule.seralize(target_pixel_rules)
        return self._get_response(locals())

    def updateTargetPixel(self, account_id, target_pixel_id, category_id, client_id=None, domain=None):
        return self._get_response(locals())
