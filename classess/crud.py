import pytest_html
import requests
import time
class Crud:
    def __init__(self,base_url):
        self.base_url=base_url

    def post(self,endpoint,payload,headers=None):
        url=self.base_url+endpoint
        res = requests.post(url=url, json=payload,headers=headers)
        return res
    def get(self,endpoint):
        url = self.base_url + endpoint
        res2=requests.get(url=url)
        return res2