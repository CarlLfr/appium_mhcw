#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/22
# @Author  : Liufeiru

import os

class BaseAdb():
    def __init__(self):
        self.udid_command = 'adb devices'
        self.platformVersion_command = 'adb shell getprop ro.build.version.release'
        self.deviceName_command = 'adb shell getprop ro.product.model'

    def get_udid(self):
        # 利用adb devices先输出所有已连接上的android devices, 然后去掉输出中无用的字符串，只保留devices SN
        devices_list = []
        result = os.popen(self.udid_command).readlines()
        # print(result)
        list_len = len(result)
        if list_len == 2:
            print("没有设备连接！")
        else:
            for i in range(list_len):
                if result[i].find('\t') != -1:
                    devices_list.append(result[i].split('\t')[0])
        # print(devices_list)
        # 返回第一个udid(通常指有一台设备进行测试)
        return devices_list[0]

    def get_platformVersion(self):
        # 获取连接设备的系统版本号platformVersion
        try:
            result = os.popen(self.platformVersion_command).read()
            platformVersion = result.split('\n')[0]
            return platformVersion
        except Exception as e:
            print(e)

    def get_deviceName(self):
        # 获取连接设备名deviceName
        try:
            result = os.popen(self.deviceName_command).read()
            deviceName = result.split('\n')[0]
            return deviceName
        except Exception as e:
            print(e)

if __name__ == '__main__':
    baseAdb = BaseAdb()
    b = baseAdb.get_deviceName()
