#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/23
# @Author  : Liufeiru

import os
import re
import subprocess
from Base.BaseConfig import APP_PATH
'''
先获取apk文件路径，再获取apk文件信息
'''

class ApkInfo():
    # 获取app文件完整路径
    def get_apk_path(self):
        # 获取App文件夹中的所有apk文件名
        package_list = os.listdir(APP_PATH)

        # 判断App包中apk文件的个数，并选择
        try:
            num = len(package_list)
            if num == 0:
                print("请添加需要测试的apk文件！")
            elif num == 1:
                apk_path = APP_PATH + package_list[0]
            elif num >= 2:
                print(package_list)
                index = int(input("请输入要测试的包名的编号（从0开始）："))
                apk_path = APP_PATH + package_list[index]
            return apk_path
        except Exception as e:
            print(e)

    # 获取应用appPackage、启动类appActivity
    def getApkInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.get_apk_path(), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode()
        # print(t)
        try:
            match_appPackage = re.compile("package: name='(.*?)'").search(t)
            match_apkActivity = re.compile("launchable activity name='(.*?)'").search(t)
            app_Package = match_appPackage.groups()[0]
            app_activity = match_apkActivity.groups()[0]
            # print(app_Package)
            return app_Package, app_activity
        except Exception as e:
            print(e)

    # 获取启动类
    # def getApkActivity(self):
    #     p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
    #                          stderr=subprocess.PIPE,
    #                          stdin=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     t = output.decode()
    #     try:
    #         match = re.compile("launchable activity name='(.*?)'").search(t)
    #         apk_activity = match.groups()[0]
    #         # print(apk_activity)
    #         return apk_activity
    #     except Exception as e:
    #         print(e)

if __name__ == '__main__':
    apkPath = get_apk_path()
    print(apkPath)
    apkInfo = ApkInfo(apkPath)
    print(apkInfo.getApkName())

