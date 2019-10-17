#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/04
# @Author  : Liufeiru

import os
import sys
import inspect

class GetCurrentItems():
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance
    def __init__(self):
        pass

    # 返回当前文件路径
    @staticmethod
    def get_current_file_path():
        return __file__

    # 返回当前文件名
    @staticmethod
    def get_current_file_name():
        return os.path.split(__file__)[-1]

    # 返回当前类名
    def get_current_class_name(self):
        return self.__class__.__name__

    # 返回当前函数名
    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    # 返回当前所在行数
    @staticmethod
    def get_current_lineno():
        return sys._getframe().f_lineno

p = GetCurrentItems()

if __name__ == '__main__':
    p = GetCurrentItems()
    print(p.get_current_file_name())