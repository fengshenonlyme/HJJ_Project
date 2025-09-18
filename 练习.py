import configparser
import json
from utils.read_data import read_yaml, get_url
import pytest
import requests


@pytest.mark.parametrize('case', read_yaml()['login'])
def test_login(case):
    url = get_url() + case['url']
    header = case['headers']
    body = case['body']
    req = requests.post(url, json=body, headers=header)
    resp = json.loads(req.text)
    assert resp['code'] == case['assert']


if __name__ == '__main__':
    test_login()
