import pytest_html
import requests
import time
class Edge:
    def __init__(self,base_url):
        self.base_url=base_url

    def post(self,endpoint,payload):
        url=self.base_url+endpoint
        res = requests.post(url=url, json=payload)
        return res