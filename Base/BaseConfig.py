#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/23
# @Author  : Liufeiru

import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 日志文件路径
LOG_PATH = BASE_PATH + '/Log/'
# Config配置文件路径
CONFIG_PATH = BASE_PATH + '/Config/'
# desired_caps.yaml路径
DESIRED_CAPS_YAML_PATH = CONFIG_PATH + 'desired_caps.yaml'
# App文件路径
APP_PATH = BASE_PATH + '/App/'
# 截图路径
SCREENSHOT_PATH = BASE_PATH + '/Screenshot/'
# 报告路径
REPORT_PATH = BASE_PATH + '/Report/'


if __name__ == '__main__':
    print(LOG_PATH)