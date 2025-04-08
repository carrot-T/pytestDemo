import os
from core.rest_client import RestClient
from common.MyDocument import Document


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def list_all_users(self, **kwargs):
        return self.get("/users", **kwargs)

    def list_one_user(self, username, **kwargs):
        return self.get("/users/{}".format(username), **kwargs)

    def select_series_v2(self, **kwargs):
        return self.post("/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc", **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    def update(self, user_id, **kwargs):
        return self.put("/update/user/{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.post("/delete/user/{}".format(name), **kwargs)

dcd_url = "https://www.dongchedi.com"
user = User(dcd_url)

# body={brand = 251,sort_new = "dcdscore_desc"}