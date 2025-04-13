from .api_module import ApiModule


class Leads(ApiModule):
    __slots__ = ()

    def checkUser(self,
                  lead_id,
                  test_result=None,
                  test_mode=False,
                  auto_start=False,
                  age=None,
                  country=None):
        return self._get_response(locals())

    def complete(self, vk_sid, secret, comment=None):
        return self._get_response(locals())

    def getStats(self,
                 lead_id,
                 secret=None,
                 date_start=None,
                 date_end=None):
        return self._get_response(locals())

    def getUsers(self,
                 offer_id,
                 secret,
                 offset=None,
                 count=100,
                 status=None,
                 reverse=False):
        return self._get_response(locals())

    def metricHit(self, data):
        return self._get_response(locals())

    def start(self,
              lead_id,
              secret,
              uid=False,
              aid=False,
              test_mode=False,
              force=False):
        return self._get_response(locals())
