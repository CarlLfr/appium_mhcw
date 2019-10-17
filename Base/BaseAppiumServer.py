#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/22
# @Author  : Liufeiru

import os
import time
from Base.BaseLog import log

class AppiumServer():
    def check_port(self):
        pass

    def start_appium(self):
        # 启动appium服务
        log.info("启动appium服务...")
        os.system("start appium -a 127.0.0.1 -p 4723 -bp 4724 --chromedriver-port 9519 -U xiaomi --session-override")
        time.sleep(8)

    def quit_appium(self):
        # 停止appium服务
        log.info("停止appium服务...")
        process = os.popen("netstat -aon |findstr 4723").read()
        # print(process)
        pid = process.replace(' ', '').split("LISTENING")[1]
        m = os.popen("taskkill -f -pid %s" % pid)
        print(m.read())

if __name__ == '__main__':
    AppiumServer = AppiumServer()
    AppiumServer.quit_appium()