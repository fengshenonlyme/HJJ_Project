from utils.read_data import read_yaml, get_url, read_token
from utils.get_token import GetToken
import pytest
import requests
import json
import os
import sys
import allure


@allure.feature('驻地信息模块')
class TestGarrison:
    @pytest.mark.parametrize('case', read_yaml()['garrison'])
    def test_garrison(self, case):
        token = read_token()
        # print(token)
        # print(case['url'])
        url = get_url() + case['url']
        # print(url)
        header = {'x-access-token': token}
        # print(header)
        req = requests.get(url,  headers=header)
        resp = json.loads(req.text)
        assert resp['code'] == case['assert']


if __name__ == '__main__':
    pytest.main()