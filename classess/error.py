import pytest_html
import requests
import time
class Error:
    def __init__(self,base_url):
        self.base_url=base_url

    def get(self,endpoint):
        url = self.base_url + endpoint
        res2=requests.get(url=url)
        return res2
    def delete(self,endpoint):
        url=self.base_url+endpoint
        res3=requests.delete(url=url)
        return res3