#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/10/09
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver

# 首页-日历
class CalendarRecord(BaseView):
    calendarIcon = (By.XPATH, '//android.widget.HorizontalScrollView[@index=0]/../../android.view.View[@index=2]')  # 记录页-日历图标
    addIcon = (By.XPATH, '//android.widget.ScrollView[@index=1]/../android.view.View[@index=2]')    # 日历记录页-“+”按钮
    clockBtn = (By.XPATH, '//android.widget.TextView[@text="日常打卡"]')    # 日常打卡
    drinkBtn = (By.XPATH, '//android.widget.TextView[@text="喝水"]/../../android.view.View[@index=2]')  # 日常打卡页-喝水图标
    backBtn = (By.XPATH, '//android.widget.TextView[@text="日常打卡"]/../android.view.View[@index=1]')  # 日常打卡页-返回按钮
    recordPageBack = (By.XPATH, '//android.widget.TextView[@text="日历记录" and @index=2]/../android.view.View[@index=1]')  # 日历记录页-返回按钮

    # 日历记录页进行日常打卡
    def calendar_daily_clock(self):
        log.info("===当前方法：%s，验证日历记录功能是否正常===" % p.get_current_function_name())

        # 进入日历记录页
        calendarIconElement = self.driver.find_element(*self.calendarIcon)
        calendarIconElement.click()
        log.info("进入日历记录页面")
        time.sleep(1)

        # 点击“+”弹窗
        addIconElement = self.driver.find_element(*self.addIcon)
        addIconElement.click()
        time.sleep(1)

        # 点击进入日常打卡页面
        clockElement = self.driver.find_element(*self.clockBtn)
        clockElement.click()
        log.info("进入日常打卡页面")
        time.sleep(1)

        # 点击喝水
        drinkElement = self.driver.find_element(*self.drinkBtn)
        drinkElement.click()
        log.info("点击喝水")
        time.sleep(1)

        # 返回至日历记录页
        backElement = self.driver.find_element(*self.backBtn)
        backElement.click()
        log.info("返回至日历记录页")
        time.sleep(1)

        # 返回至记录页
        recordPageBackEle = self.driver.find_element(*self.recordPageBack)
        recordPageBackEle.click()
        log.info("日历记录页返回至日历页")
        time.sleep(1)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    calendar = CalendarRecord(driver)
    calendar.calendar_daily_clock()