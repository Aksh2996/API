import pytest_html
import requests
import time
class Perf:
    def __init__(self,base_url):
        self.base_url=base_url
    def post2(self,endpoint,payload):
        url=self.base_url+endpoint
        res = requests.post(url=url,json=payload)
        return res
    def post(self,endpoint):
        url=self.base_url+endpoint
        res = requests.post(url=url)
        return res
    def get(self,endpoint):
        url = self.base_url + endpoint
        res2=requests.get(url=url)
        return res2