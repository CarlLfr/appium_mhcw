#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/09
# @Author  : Liufeiru

import os
import time
from Base.BaseConfig import REPORT_PATH

def report_path():
    reportPath = os.path.join(REPORT_PATH, '{}_report.html'.format(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))))
    return reportPath

if __name__ == '__main__':
    print(report_path())