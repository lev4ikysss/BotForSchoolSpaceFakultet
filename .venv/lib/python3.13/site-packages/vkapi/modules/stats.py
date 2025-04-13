from .api_module import ApiModule


class Stats(ApiModule):
    __slots__ = ()

    def get(self,
            group_id=None,
            app_id=None,
            timestamp_from=None,
            timestamp_to=None,
            interval='day',
            intervals_count=None,
            filters=None,
            stats_groups=None,
            extended=True):
        return self._get_response(locals())

    def getPostReach(self, owner_id, post_id):
        return self._get_response(locals())

    def trackVisitor(self):
        return self._get_response(locals())
