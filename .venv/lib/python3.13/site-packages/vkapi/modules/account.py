from .api_module import ApiModule


class Account(ApiModule):
    __slots__ = ()

    def ban(self, owner_id):
        return self._get_response(locals())

    def changePassword(self, new_password, old_password=None, restore_sid=None, change_password_hash=None):
        return self._get_response(locals())

    def getActiveOffers(self, offset=0, count=100):
        return self._get_response(locals())

    def getAppPermissions(self, user_id):
        return self._get_response(locals())

    def getBanned(self, offset=None, count=20):
        return self._get_response(locals())

    def getCounters(self, _filter=None):
        return self._get_response(locals())

    def getInfo(self, fields=None):
        return self._get_response(locals())

    def getProfileInfo(self):
        return self._get_response(locals())

    def getPushSettings(self, device_id):
        return self._get_response(locals())

    def registerDevice(self,
                       token,
                       device_id,
                       device_model=None,
                       device_year=None,
                       system_version=None,
                       settings=None,
                       sandbox=False):
        return self._get_response(locals())

    def saveProfileInfo(self,
                        first_name=None,
                        last_name=None,
                        maiden_name=None,
                        screen_name=None,
                        cancel_request_id=None,
                        sex=None,
                        relation=None,
                        relation_partner_id=None,
                        bdate=None,
                        bdate_visibility=None,
                        home_town=None,
                        country_id=None,
                        city_id=None,
                        status=None):
        return self._get_response(locals())

    def setInfo(self, name, value):
        return self._get_response(locals())

    def setNameInMenu(self, user_id, name=None):
        return self._get_response(locals())

    def setOffline(self):
        return self._get_response(locals())

    def setOnline(self, voip=None):
        return self._get_response(locals())

    def setPushSettings(self, device_id, settings=None, key=None, value=None):
        return self._get_response(locals())

    def setSilenceMode(self, device_id=None, time=None, peer_id=None, sound=None):
        return self._get_response(locals())

    def unban(self, owner_id):
        return self._get_response(locals())

    def unregisterDevice(self, device_id=None, sandbox=False):
        return self._get_response(locals())
