#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/10/10
# @Author  : Liufeiru

import time
from Base.BaseDriver import BaseDriver
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseMethod import is_exist_element

# 验证意见反馈功能是否正常
class Feedback(BaseView):
    feedbackBtn = (By.XPATH, '//android.widget.TextView[@text="意见反馈"]') # 我的页面-意见反馈按钮
    pre_feedbackBox = (By.XPATH, '//android.widget.TextView[@text="期待您的宝贵意见"]') # 意见反馈页面-输入框
    feedbackBox = (By.XPATH, '//android.widget.EditText[@text="请留下您的意见或建议"]')   # 意见反馈页面-跳转后输入框
    submitBtn = (By.XPATH, '//android.widget.TextView[@text="提交"]') # 意见反馈页面-提交按钮
    feed_content = "abcdefghijklmn"

    # 意见反馈
    def feedback(self):
        log.info("===当前方法：%s，验证意见反馈功能===" % p.get_current_function_name())

        # 我的页面点击意见反馈
        feedbackElement = self.driver.find_element(*self.feedbackBtn)
        feedbackElement.click()
        log.info("进入意见反馈页面")
        time.sleep(0.5)

        # 填写意见
        pre_feedbackEle = self.driver.find_element(*self.pre_feedbackBox)
        pre_feedbackEle.click()
        time.sleep(0.5)
        feedbackBoxEle = self.driver.find_element(*self.feedbackBox)
        feedbackBoxEle.send_keys(self.feed_content)
        time.sleep(0.5)

        # 提交
        submitElement = self.driver.find_element(*self.submitBtn)
        # 点击两次提交按钮，第一次点击隐藏键盘
        submitElement.click()
        time.sleep(0.5)
        submitElement.click()
        time.sleep(1)

        # 判断是否提交成功
        boo = is_exist_element(self.driver, self.feed_content)
        if boo == True:
            log.info("意见反馈提交成功！")
        else:
            log.error("意见反馈提交失败！")


if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    feedback = Feedback(driver)
    feedback.feedback()