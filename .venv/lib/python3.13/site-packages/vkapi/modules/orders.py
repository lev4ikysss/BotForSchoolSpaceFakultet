from .api_module import ApiModule


class Orders(ApiModule):
    __slots__ = ()

    def cancelSubscription(self, user_id, subscription_id, pending_cancel=False):
        return self._get_response(locals())

    def changeState(self, order_id, action, app_order_id=None, test_mode=False):
        return self._get_response(locals())

    def get(self, offset=0, count=100, test_mode=False):
        return self._get_response(locals())

    def getAmount(self, user_id, votes):
        return self._get_response(locals())

    def getById(self, order_id=None, order_ids=None, test_mode=False):
        return self._get_response(locals())

    def getUserSubscriptionById(self, user_id, subscription_id):
        return self._get_response(locals())

    def getUserSubscriptions(self, user_id):
        return self._get_response(locals())

    def updateSubscriptions(self, user_id, subscription_id, price):
        return self._get_response(locals())
