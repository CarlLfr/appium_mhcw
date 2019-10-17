#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/04
# @Author  : Liufeiru

import os
import time
from Base.BaseConfig import SCREENSHOT_PATH
from Base.BaseTools import p

'''
封装截图并保存的方法
'''

class ScreenShot():
    def __init__(self, driver, screenShotName):
        self.driver = driver
        self.screenShotName = screenShotName

    # 获取当前时间戳
    def get_day(self):
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        return day

    def get_time(self):
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        return tm

    # 获取文件夹路径，不存在则创建
    def make_dir(self):
        day = self.get_day()
        dir_path = SCREENSHOT_PATH + day
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        return dir_path

    # 截图
    def screen_shot(self):
        dir_path = self.make_dir()
        tm = self.get_time()
        path = dir_path + '/' + tm + self.screenShotName + '.png'
        self.driver.get_screenshot_as_file(path)

if __name__ == '__main__':
    # s = ScreenShot(driver, screenShotName)
    # s.make_dir()
    pass