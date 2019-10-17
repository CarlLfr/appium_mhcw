#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import time
from BSTestRunner import BSTestRunner
from Base.BaseUpdateYmal import UpdateYaml
from Base.BaseInstallApp import IsInstallApp
from Base.BaseAppiumServer import AppiumServer
from Base.BaseDriver import BaseDriver
from Base.BaseLog import log
from Base.BaseView import BaseView
from Base.BaseOperate import BaseOperate
from Base.BaseMethod import is_exist_element
from Base.BaseReport import report_path
from selenium.webdriver.common.by import By
from Base.BaseScreenShot import ScreenShot
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from Testcase.test_01_launch_app import LaunchApp
from Testcase.test_02_noLogin import NoLogin
from Testcase.test_03_register import Register
from Testcase.test_04_login import LoginOut
from Testcase.test_05_daily_clock import DailyClick
from Testcase.test_06_warning import WarningBar
from Testcase.test_07_health import HealthManagement
from Testcase.test_08_chose_pet import ChosePet
from Testcase.test_09_calendar_record import CalendarRecord
from Testcase.test_10_integral import IntegralSignIn
from Testcase.test_11_feedback import Feedback


class CaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        UpdateYaml().update_desired_caps()  # 获取APP信息、手机信息，写入ymal文件
        IsInstallApp().is_install_app() # 判断测试手机是否已经安装需要测试的APP，否则安装
        AppiumServer().start_appium()   # 启动Appium服务
        cls.driver = BaseDriver().Android_driver()   # 启动App
        return cls.driver

    def setUp(self):
        pass

    def test_001_launchApp(self):
        '''启动APP，进入首页'''
        LaunchApp(self.driver).check_permitBin()
        time.sleep(5)

    def test_002_noLogin_cancel(self):
        '''验证未登录状态，点击按钮是否弹窗提示去登录'''
        NoLogin(self.driver).chose_pet_click()
        time.sleep(5)

    def test_003_noLogin_switch_to_academy(self):
        '''验证未登录状态能否查看学院文章'''
        NoLogin(self.driver).switch_page()
        time.sleep(5)

    def test_004_register_protocol(self):
        '''验证注册-查看《用户注册及隐私协议》功能'''
        Register(self.driver).get_in_protocol()
        time.sleep(5)

    def test_005_register_old(self):
        '''验证注册-输入已注册过的手机号进行注册'''
        Register(self.driver).old_user_register()
        time.sleep(5)

    @unittest.skip("跳过输入未注册过的手机号进行注册")
    def test_006_register_new(self):
        '''验证注册-输入未注册过的手机号进行注册，并添加宠物功能'''
        Register(self.driver).new_register()
        time.sleep(5)

    @unittest.skip("跳过验证码登录")
    def test_007_login_code(self):
        '''验证登录-验证码登录功能'''
        LoginOut(self.driver).code_login()
        time.sleep(5)

    @unittest.skip("跳过微信登录")
    def test_008_login_weiXin(self):
        '''验证登录-微信登录功能'''
        LoginOut(self.driver).weixin_login()
        time.sleep(5)

    def test_009_login_pwd(self):
        '''验证登录-密码登录功能'''
        LoginOut(self.driver).password_login()
        time.sleep(5)

    def test_010_add_item(self):
        '''验证日常打卡-添加功能'''
        DailyClick(self.driver).add_item()
        time.sleep(5)

    def test_011_daily_click(self):
        '''验证日常打卡-打卡功能'''
        DailyClick(self.driver).daily_click()
        time.sleep(5)

    def test_012_delete_item(self):
        '''验证日常打卡-删除打卡项功能'''
        DailyClick(self.driver).delete_item()
        time.sleep(5)

    def test_013_add_warning(self):
        '''验证提醒吧-新增提醒功能'''
        WarningBar(self.driver).add_warning()
        time.sleep(5)

    def test_014_finished_warning(self):
        '''验证提醒吧-点击完成提醒功能'''
        WarningBar(self.driver).finished_warning()
        time.sleep(5)

    def test_015_delete_warning(self):
        '''验证提醒吧-删除提醒项功能'''
        WarningBar(self.driver).delete_warning()
        time.sleep(5)

    def test_016_add_health_item(self):
        '''验证健康管理-新增功能'''
        HealthManagement(self.driver).add_health_item()
        time.sleep(5)

    def test_017_change_health_item(self):
        '''验证健康管理-修改功能'''
        HealthManagement(self.driver).change_health_item()
        time.sleep(5)

    def test_018_delete_health_item(self):
        '''验证健康管理-删除功能'''
        HealthManagement(self.driver).delete_health_item()
        time.sleep(5)

    def test_019_change_pet(self):
        '''验证切换宠物功能'''
        ChosePet(self.driver).change_pet()
        time.sleep(5)

    def test_020_add_pet(self):
        '''验证添加宠物功能'''
        ChosePet(self.driver).add_pet()
        time.sleep(5)

    def test_021_delete_pet(self):
        '''验证删除宠物功能'''
        ChosePet(self.driver).delete_pet()
        time.sleep(5)

    def test_022_calendar_daily_clock(self):
        '''验证首页日历功能（选择日常打卡功能进行验证）'''
        CalendarRecord(self.driver).calendar_daily_clock()
        time.sleep(5)

    def test_023_integral_sign_in(self):
        '''验证积分-签到功能'''
        IntegralSignIn(self.driver).integral_sign_in()
        time.sleep(5)

    def test_024_feedback(self):
        '''验证意见反馈功能'''
        Feedback(self.driver).feedback()
        time.sleep(5)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        AppiumServer().quit_appium()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    CaseTestList = [CaseTest("test_001_launchApp"), CaseTest("test_002_noLogin_cancel"), CaseTest("test_003_noLogin_switch_to_academy"), CaseTest("test_004_register_protocol"),
                    CaseTest("test_005_register_old"), CaseTest("test_009_login_pwd"), CaseTest("test_010_add_item"), CaseTest("test_011_daily_click"),
                    CaseTest("test_012_delete_item"), CaseTest("test_013_add_warning"), CaseTest("test_014_finished_warning"), CaseTest("test_015_delete_warning"), CaseTest("test_016_add_health_item"),
                    CaseTest("test_017_change_health_item"), CaseTest("test_018_delete_health_item"), CaseTest("test_019_change_pet"), CaseTest("test_020_add_pet"), CaseTest("test_021_delete_pet"),
                    CaseTest("test_022_calendar_daily_clock"), CaseTest("test_023_integral_sign_in"), CaseTest("test_024_feedback")]
    # CaseTestList = [CaseTest("test_001_launchApp"), CaseTest("test_002_noLogin_cancel")]
    suite.addTests(CaseTestList)

    html_file = report_path()
    with open(html_file, 'wb') as f:
        runner = BSTestRunner(stream=f, title="麻花宠物APP自动化测试报告", description="Appium自动化测试报告")
        runner.run(suite)

