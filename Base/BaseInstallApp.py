#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/04
# @Author  : Liufeiru

import os
from time import sleep
from ruamel import yaml
from Base.BaseLog import log
from multiprocessing import Process
from Base.BaseConfig import DESIRED_CAPS_YAML_PATH

# 从yaml文件中读取App信息
def get_appInfo():
    with open(DESIRED_CAPS_YAML_PATH, 'r') as f:
        content = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
        appPath = content['app']
        appName = appPath.split('/')[-1]
        appPackage = content['appPackage']
    return appPath, appName, appPackage


'''
安装APP、卸载APP、判断是否已经安装APP
'''
class IsInstallApp():
    def __init__(self):
        self.appPath, self.appName, self.appPackage = get_appInfo()
        self.install_command = 'adb install ' + self.appPath
        self.uninstall_command = 'adb uninstall ' + self.appPackage
        self.list_package_command = 'adb shell pm list package'

    # 判断设备是否已经安装应用，未安装则安装应用
    def is_install_app(self):
        global flag
        log.info("---检查{}应用是否已安装---".format(self.appName))
        result = os.popen(self.list_package_command).read()
        if self.appPackage in result:
            log.info("---应用已安装---")
            pass
        else:
            log.info("---应用未安装，开始安装---")
            self.adb_install_main()

    # 安装APP基本方法
    def install_app(self):
        try:
            log.info("正在安装apk文件，请稍后...")
            result = os.popen(self.install_command).read()
            if "Success" in result:
                log.info("---{}应用安装成功---".format(self.appName))
        except Exception as e:
            log.error("---{}应用安装失败，失败原因为{}---".format(self.appName, e))

    # 监控APP安装确认弹窗，并点击"继续安装"按钮
    def install_for_uiautomation(self):
        # log.info("---开启线程监控APP安装确认弹窗---")
        # _install = device(text="继续安装")
        # num = 0
        # while num < 6:
        #     num += 1
        #     print("第{}次".format(num))
        #     sleep(5)
        #     if _install.exists:
        #         _install.click()
        #         break

        log.info("---开启线程监控APP安装确认弹窗---")
        # sleep(15)
        num = 0
        while num < 5:
            num += 1
            print("第{}次".format(num))
            sleep(5)
            os.system("adb shell input tap 370 2430")

    # 同时开启监控弹窗线程与APP安装基本方法线程，进行app安装
    def adb_install_main(self):
        p1 = Process(target=self.install_app, args=())
        p2 = Process(target=self.install_for_uiautomation, args=())

        p1.start()
        p2.start()
        p1.join()
        p2.join()

    # 卸载app
    def uninstall_app(self):
        try:
            result = os.popen(self.uninstall_command).read()
            if "Success" in result:
                log.info("---{}应用卸载成功---".format(self.appName))
        except Exception as e:
            log.error("---{}应用卸载失败，失败原因为{}---".format(self.appName, e))


if __name__ == '__main__':
    i = IsInstallApp()
    result = i.is_install_app()