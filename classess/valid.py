import pytest_html
import requests
import time
class Valid:
    def __init__(self,base_url):
        self.base_url=base_url

    def post(self,endpoint,payload,headers=None):
        url=self.base_url+endpoint
        res = requests.post(url=url, json=payload,headers=headers)
        return res