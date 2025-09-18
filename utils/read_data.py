import yaml
import os
import configparser


def get_url():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ini_path = os.path.join(current_dir, '../config/config.ini')

    config = configparser.ConfigParser()

    # 读取ini文件
    config.read(ini_path, encoding='utf-8')

    # 获取配置值（最简单的方式）
    url = config.get('url', 'url1')

    # print(url)
    return url


def read_yaml():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, '../testcase/login.yaml')
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        # print(data)
        return data


if __name__ == '__main__':
    # read_yaml()
    get_url()