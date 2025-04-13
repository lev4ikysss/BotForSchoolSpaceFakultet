from .api_module import ApiModule


class Users(ApiModule):
    __slots__ = ()

    def get(self, user_ids=None, fields=None, name_case='nom'):
        return self._get_response(locals())

    def getFollowers(self, user_id=None, offset=None, count=100, fields=None, name_case='nom'):
        return self._get_response(locals())

    def getSubscriptions(self, user_id=None, extended=False, offset=None, count=20, fields=None):
        return self._get_response(locals())

    def isAppUser(self, user_id=None):
        return self._get_response(locals())

    def report(self, user_id, _type, comment=None):
        return self._get_response(locals())

    def search(self,
               q=None,
               sort=None,
               offset=None,
               count=20,
               fields=None,
               city=None,
               country=None,
               hometown=None,
               university_country=None,
               university=None,
               university_year=None,
               university_faculty=None,
               university_chair=None,
               sex=None,
               status=None,
               age_from=None,
               age_to=None,
               birth_day=None,
               birth_month=None,
               birth_year=None,
               online=None,
               has_photo=None,
               school_country=None,
               school_city=None,
               school_class=None,
               school=None,
               region=None,
               interests=None,
               company=None,
               position=None,
               group_id=None,
               from_list=None):
        return self._get_response(locals())
