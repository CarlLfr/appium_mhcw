#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/31
# @Author  : Liufeiru

from ruamel import yaml
from Base.BaseAdb import BaseAdb
from Base.BaseApk import ApkInfo
from Base.BaseConfig import DESIRED_CAPS_YAML_PATH
from Base.BaseLog import log

'''
更新desired_caps中的设备及.apk信息
'''

class UpdateYaml():
    def __init__(self):
        self.platformVersion = BaseAdb().get_platformVersion()
        self.deviceName = BaseAdb().get_deviceName()
        self.udid = BaseAdb().get_udid()
        self.app = ApkInfo().get_apk_path()
        self.appPackage, self.appActivity = ApkInfo().getApkInfo()
        self.yamlPath = DESIRED_CAPS_YAML_PATH

    def update_desired_caps(self):
        # 读取yaml中的内容并修改
        log.info("开始更新desired_caps.ymal中的APP及手机参数...")
        try:
            with open(self.yamlPath, 'r', encoding='utf-8') as f:
                content = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
                content['platformVersion'] = self.platformVersion
                content['deviceName'] = self.deviceName
                content['udid'] = self.udid
                content['app'] = self.app
                content['appPackage'] = self.appPackage
                content['appActivity'] = self.appActivity

            # 将修改的内容重新写入该yaml文件
            with open(self.yamlPath, 'w', encoding='utf-8') as nf:
                yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)
            log.info("---desired_caps.ymal更新完成---")
        except Exception as e:
            log.info(e)

if __name__ == '__main__':
    updateYaml = UpdateYaml()
    updateYaml.update_desired_caps()