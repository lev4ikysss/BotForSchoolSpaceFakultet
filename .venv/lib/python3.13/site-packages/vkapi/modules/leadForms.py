from .api_module import ApiModule


class LeadForms(ApiModule):
    __slots__ = ()

    def create(self,
               group_id,
               name,
               title,
               description,
               questions,
               policy_link_url,
               photo=None,
               confirmation=None,
               site_link_url=None,
               active=False,
               once_per_user=False,
               pixel_code=None,
               notify_admins=None,
               notify_emails=None):
        questions = ApiModule.seralize(questions)
        return self._get_response(locals())

    def delete(self, group_id, form_id):
        return self._get_response(locals())

    def get(self, group_id, form_id):
        return self._get_response(locals())

    def getLeads(self, group_id, form_id, limit=10, next_page_token=None):
        return self._get_response(locals())

    def getUploadURL(self):
        return self._get_response(locals())

    def list(self, group_id):
        return self._get_response(locals())

    def update(self,
               group_id,
               form_id,
               name,
               title,
               description,
               questions,
               policy_link_url,
               photo=None,
               confirmation=None,
               site_link_url=None,
               active=False,
               once_per_user=False,
               pixel_code=None,
               notify_admins=None,
               notify_emails=None):
        questions = ApiModule.seralize(questions)
        return self._get_response(locals())
