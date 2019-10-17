#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/23
# @Author  : Liufeiru

import time
import os
import logging
from Base.BaseConfig import LOG_PATH

class BaseLog():
    def __init__(self):

        # 日志文件命名
        self.logName = os.path.join(LOG_PATH, '%s.log' % time.strftime('%Y_%m_%d'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s')


    def __console(self, level, message):
        # 创建一个FileHandler用于写到本地
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler用于输出到控制台
        ch= logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('waring', message)

    def error(self, message):
        self.__console('error', message)

log = BaseLog()

if __name__ == '__main__':
    log = BaseLog()
    log.info("---测试开始---")
    log.info("操作步骤1,2,3")
    log.warning("---测试结束---")