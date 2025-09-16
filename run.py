import os
import time
import shutil
import allure
import pytest

if __name__ == '__main__':
    shutil.rmtree('./report')
    shutil.rmtree('./result')
    pytest.main(["-sv", "./test_code/UI_Code/红色",
                 "--alluredir", "./result"])
    os.system("allure generate ./result -o ./report --clean")