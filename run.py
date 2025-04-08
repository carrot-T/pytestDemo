import os
import pytest
from common.logger import logger


if __name__ == '__main__':
    pytest.main(['./testcases/test_U2.py'])

    # 将测试报告转为html格式
    res = os.system("allure generate ./report/result/ -o ./report/html --clean")

