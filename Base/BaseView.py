#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/04
# @Author  : Liufeiru

# 封装基类
class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)