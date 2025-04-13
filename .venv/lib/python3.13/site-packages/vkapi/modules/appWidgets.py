from .api_module import ApiModule


class AppWidgets(ApiModule):
    __slots__ = ()

    def getAppImageUploadServer(self, image_type):
        return self._get_response(locals())

    def getAppImages(self, offset=None, count=None, image_type=None):
        return self._get_response(locals())

    def getGroupImageUploadServer(self, image_type=None):
        return self._get_response(locals())

    def getGroupImages(self, offset=None, count=None, image_type=None):
        return self._get_response(locals())

    def getImagesById(self, images=None):
        return self._get_response(locals())

    def saveAppImage(self, _hash, image):
        return self._get_response(locals())

    def saveGroupImage(self, _hash=None, image=None):
        return self._get_response(locals())

    def update(self, code, _type):
        return self._get_response(locals())
