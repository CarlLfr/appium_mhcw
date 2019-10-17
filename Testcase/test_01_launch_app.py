#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/04
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver
from Base.BaseScreenShot import ScreenShot
from Base.BaseOperate import BaseOperate, page_click
from Base.BaseMethod import get_yaml_value
from Base.BaseMethod import is_exist_element

'''
启动app，首次启动授权定位弹窗、启动页、引导页、新手指引
'''
class LaunchApp(BaseView):
    permitBtn = (By.ID, 'android:id/button1')
    updateBtn = (By.XPATH, '//android.widget.TextView[@text="立即升级"]')
    XBtn = (By.XPATH, '//android.view.View[@index=1]')

    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录" and @index=1]/..') # 发现

    # 确认是否有定位弹窗
    def check_permitBin(self):
        log.info("===当前方法：%s, 启动APP，确认是否有定位弹窗，是否有引导页、新手指引、升级弹窗，有则跳过进入首页===" % p.get_current_function_name())

        try:
            permitElement = self.driver.find_element(*self.permitBtn)
            log.info("定位弹窗-允许，启动页截图中...")
            ScreenShot(self.driver, "启动页截图").screen_shot()
        except NoSuchElementException:
            ScreenShot(self.driver, "启动页截图").screen_shot()
            log.info("没有定位弹窗，判断是否有引导页...")

            # 根据yaml文件中noReset的值判断是否有引导页，true重启，false不重启
            noReset = get_yaml_value("noReset")
            # print(noReset)
            if noReset == True:
                log.info("无引导页，进入首页")
            elif noReset == False:
                self.viewpager()
        else:
            permitElement.click()
            time.sleep(1)
            self.viewpager()

    # 引导页滑动，截图(4个页面)
    def viewpager(self):
        log.info("进入引导页，截图、滑动")

        for i in range(3):
            # 截图
            name = "引导页-" + str(i+1)
            ScreenShot(self.driver, name).screen_shot()
            # 左滑
            BaseOperate(self.driver).swipeLeft()
            time.sleep(0.5)

        log.info("点击引导页[立即体验]按钮进入首页")

        # 点击开始记录按钮，进入首页，判断是否有升级弹窗，再进入记录页点击跳过新手指引
        page_click(730, 2430)
        time.sleep(2)
        self.is_update()
        self.guide_page()

    # 记录页新手指引(3个页面)
    def guide_page(self):
        # 首页切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("首页跳转至发现页，跳过新手指引")
        time.sleep(1)

        x, y = BaseOperate(self.driver).get_size()
        for i in range(3):
            name = "新手指引-" + str(i+1)
            ScreenShot(self.driver, name).screen_shot()
            page_click(x*0.5, y*0.5)
            time.sleep(0.1)

        log.info("点击完成跳过新手指引")

    # 判断是否有升级弹窗，有则点击X号取消升级
    def is_update(self):
        boo = is_exist_element(self.driver, "立即升级")
        if boo == True:
            X = self.driver.find_element(*self.XBtn)
            X.click()
            log.info("存在升级弹窗，点击X取消升级")
        else:
            log.info("不存在升级弹窗，进入首页")
        time.sleep(2)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    launch = LaunchApp(driver)
    launch.check_permitBin()