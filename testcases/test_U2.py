import os

import pytest
import allure

from common.logger import logger
import uiautomator2 as u2
from uiautomator2.image import imread, compare_ssim

d = u2.connect()

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("验证框架功能")
@allure.feature("allure报告生成")
class TestU2:

    @allure.story("用例--获取全部用户信息")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    # @pytest.mark.single
    def test_001(self):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step('打开今日头条$$$$$$$$$$$$后再回到主页'):
            d.app_start("com.ss.android.article.news")
            d.sleep(5)
            d.press("home")
        with allure.step('check 真'):
            assert True

    @allure.story("-----story----")
    @allure.description("description---")
    # @pytest.mark.single
    def test_002(self):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step('步骤一'):
            print("步骤一")
        with allure.step('步骤二'):
            assert True


if __name__ == '__main__':
    pytest.main(['test_U2.py'])
