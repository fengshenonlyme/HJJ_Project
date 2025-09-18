import configparser
import json
import os
import sys

import allure

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from utils.read_data import read_yaml, get_url
import pytest
import requests


@allure.feature('登录模块')
class TestLogin:
    @pytest.mark.parametrize('case', read_yaml()['login'])
    def test_login(self, case):
        url = get_url() + case['url']
        print(url)
        header = case['headers']
        print(header)
        body = case['body']
        req = requests.post(url, json=body, headers=header)
        resp = json.loads(req.text)
        print(resp)
        assert resp['code'] == case['assert']


if __name__ == '__main__':
    pytest.main()
