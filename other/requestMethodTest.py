from unittest import TestCase
import requests


class TestRequestMethod(TestCase):
    base_url = 'http://192.168.1.100:8000/login'

    def testGetMethod(self):
        rep = requests.get(url=self.base_url, json={"username": "admin", "password": "123456"},
                           proxies={"http": "127.0.0.1:8080"})
        print(rep.json())

    def testPostMethod(self):
        rep = requests.post(url=self.base_url, data={'username': 'admin', 'passwogrd': '123456'})
        print(rep.text)
