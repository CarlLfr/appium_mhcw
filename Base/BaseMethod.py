#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/05
# @Author  : Liufeiru

from ruamel import yaml
from Base.BaseConfig import DESIRED_CAPS_YAML_PATH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 封装方法，读取desired_caps.yaml中的内容
def get_yaml_value(key):
    with open(DESIRED_CAPS_YAML_PATH, 'r') as f:
        content = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
        val = content[key]
    return val

# 封装方法，判断元素是否存在
def is_exist_element(driver, element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False

# 封装方法，判断toast是否存在
def is_exist_toast(driver, text, timeout=5, poll_frequency=0.1):
    # 最大超时时间默认为5s，时间间隔默认0.1s查询一次，text为toast内容
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False