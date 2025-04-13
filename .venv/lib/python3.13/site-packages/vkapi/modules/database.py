from .api_module import ApiModule


class Database(ApiModule):
    __slots__ = ()

    def getChairs(self, faculty_id, offset=None, count=100):
        return self._get_response(locals())

    def getCities(self, country_id, region_id=None, q=None, need_all=None, offset=None, count=100):
        return self._get_response(locals())

    def getCitiesById(self, city_ids=None):
        return self._get_response(locals())

    def getCountries(self, need_all=None, code=None, offset=None, count=100):
        return self._get_response(locals())

    def getCountriesById(self, country_ids=None):
        return self._get_response(locals())

    def getFaculties(self, university_id, offset=None, count=100):
        return self._get_response(locals())

    def getMetroStations(self, city_id, offset=None, count=100, extended=0):
        return self._get_response(locals())

    def getMetroStationsById(self, station_id=None):
        return self._get_response(locals())

    def getRegions(self, country_id, q=None, offset=None, count=100):
        return self._get_response(locals())

    def getSchoolClasses(self, country_id=None):
        return self._get_response(locals())

    def getSchools(self, city_id, q=None, offset=None, count=100):
        return self._get_response(locals())

    def getUniversities(self, q=None, country_id=None, city_id=None, offset=None, count=100):
        return self._get_response(locals())
