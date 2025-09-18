import time

import requests
import configparser
import json

import yaml


class Pass:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../config/config.ini')

    def get_token(self):
        code = input("请输入图形验证码: ")
        url = self.config.get('url', 'url1') + '/api/military-user-service/uc/login/login'
        # print(url)
        # print(url)
        header = {
            "content-type": "application/json;charset=UTF-8"
        }
        body = {
            "username": self.config.get('url', 'username'),
            "password": self.config.get('url', 'password'),
            'checkKey': 1629428467008,
            'captcha': str(code)
        }
        # print(body)
        req = requests.post(url, data=json.dumps(body), headers=header)
        response = json.loads(req.text)
        token = response['result']['token']
        # print(token)
        return token

    def read_yaml_basic(self):
        with open('../config/token.yaml', 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data

    def save_token(self):
        token = self.read_yaml_basic()
        url = self.config.get('url', 'url1') + f"/api/sys/rule/list?_t={int(time.time() * 1000)}"
        header = {
            'x-access-token': token
        }
        req = requests.get(url, headers=header)
        response = json.loads(req.text)
        # print(response)
        if response['code'] == 200:
            print('token生效中')
        else:
            new_token = self.get_token()
            file_path = '../config/token.yaml'
            try:
                # 先以写入模式打开文件清空内容
                with open(file_path, 'w', encoding='utf-8') as file:
                    pass  # 这会将文件截断为空

                # 然后写入新数据
                with open(file_path, 'w', encoding='utf-8') as file:
                    yaml.dump(new_token, file, allow_unicode=True, sort_keys=False)

                print(f"成功清除并写入数据到 {file_path}")

            except Exception as e:
                print(f"操作失败: {str(e)}")


if __name__ == '__main__':
    Pass().save_token()
