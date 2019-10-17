#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/23
# @Author  : Liufeiru

import time
import yaml
from appium import webdriver
from Base.BaseConfig import *
from Base.BaseAdb import BaseAdb
from Base.BaseApk import ApkInfo
from Base.BaseAppiumServer import AppiumServer



class BaseDriver():

    def Android_driver(self):
        # 从desired_caps.yaml读取配置数据
        stream = open(DESIRED_CAPS_YAML_PATH, 'r')
        data = yaml.load(stream)

        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = data['udid']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noReset'] = data['noReset']
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps['automationName'] = data['automationName']

        # 设置收到下一条命令的超时时间,超时appium会自动关闭session ,默认60秒
        desired_caps['newCommondTimeout'] = data['newCommondTimeout']

        driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
        driver.implicitly_wait(8)
        return driver

    def ios_driver(self):
        pass

if __name__ == '__main__':
    # AppiumServer().start_appium()
    # time.sleep(10)
    baseDriver = BaseDriver()
    driver = baseDriver.Android_driver()
