from .api_module import ApiModule


class PrettyCards(ApiModule):
    __slots__ = ()

    def create(self, owner_id, photo, title, link, price=None, price_old=None, button=None):
        return self._get_response(locals())

    def delete(self, owner_id, card_id):
        return self._get_response(locals())

    def edit(self, owner_id, card_id, photo=None, title=None, link=None, price=None, price_old=None, button=None):
        return self._get_response(locals())

    def get(self, owner_id, offset=0, count=10):
        return self._get_response(locals())

    def getById(self, owner_id, card_ids):
        return self._get_response(locals())

    def getUploadURL(self):
        return self._get_response(locals())
