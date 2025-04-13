from .modules.api_module import get_response, upload_file


class API:
    def __init__(self, access_token, api_version='5.101', lang='en', throwing_errors=True, raw_response=False):
        self.__dict__ = {}
        self._api_url = 'https://api.vk.com/method/'
        self._throwing_errors = throwing_errors
        self._raw_response = raw_response
        self.upload_file = upload_file
        self._params = {
            'access_token': access_token,
            'v': api_version,
            'lang': lang
        }

    def call_method(self, name, params=None):
        url = f'{self._api_url}{name}'
        pars = self._params.copy()
        if params:
            pars.update(params)
        return get_response(url, pars, self._throwing_errors, self._raw_response)

    def edit_token(self, access_token):
        self._params.update({'access_token': access_token})

    def edit_lang(self, lang):
        self._params.update({'lang': lang})

    def import_group(self, group_name):
        module_name = group_name.lower()
        class_name = module_name[0].upper() + module_name[1:]
        try:
            exec(f'from .modules.{module_name} import {class_name}')
            exec(f'self.__dict__["{module_name}"] = {class_name}(self._params, "{self._api_url}{module_name}", {self._throwing_errors}, {self._raw_response})')
            print('Group successfully imported.')
        except ImportError:
            print(f'"{group_name}" group not found.')
