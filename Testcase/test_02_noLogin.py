#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/05
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver
from Base.BaseMethod import is_exist_element
from Base.BaseScreenShot import ScreenShot
from Base.BaseOperate import page_click

# 未登录状态下功能验证
class NoLogin(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录" and @index=1]/..')  # 发现
    chosePetBtn = (By.XPATH, '//android.widget.TextView[@text="添加宠物"]') # 记录页-[选择宠物]按钮
    goLoginBtn = (By.XPATH, '//android.widget.TextView[@text="去登录"]')   # 登录弹窗-[去登录]按钮
    cancelBtn = (By.XPATH, '//android.widget.TextView[@text="取消"]') # 登录弹窗-[取消]按钮
    notLoginBtn = (By.XPATH, '//android.widget.TextView[@text="未登录"]')  # 记录页-未登录文字
    returnBtn = (By.XPATH, '//android.view.View[@index=1]') # 登录页-[返回]按钮
    getCodeBtn = (By.XPATH, '//android.widget.TextView[@text="获取验证码"]') # 登录页-[获取验证码]按钮
    academyBtn = (By.XPATH, '//android.widget.TextView[@text="学院"]')  # 学院tab
    feedCatReadyBtn = (By.XPATH, '//android.widget.TextView[@text="养猫准备"]')   # 学院-喵星人-养猫准备
    contentBtn = (By.XPATH, '//android.widget.TextView[@text="新手养猫准备指南——下篇"]')    # 养猫准备文章


    # 未登录状态，点击页面元素弹窗提示去登录，再点击[取消]按钮
    def chose_pet_click(self):
        log.info("===当前方法：%s，验证未登录状态点击按钮是否弹窗提示去登录===" % p.get_current_function_name())
        try:
            # 首页切换至记录页
            recordElement = self.driver.find_element(*self.recordBtn)
            recordElement.click()
            log.info("首页跳转至发现页")
            time.sleep(1)

            # 记录页点击添加宠物
            chosePetEle = self.driver.find_element(*self.chosePetBtn)
            chosePetEle.click()
            time.sleep(1)

            # 点击登录提示弹窗-[取消]按钮
            cancelElement = self.driver.find_element(*self.cancelBtn)
            cancelElement.click()
            time.sleep(1)
        except Exception as e:
            log.error("首页，点击[选择宠物]按钮弹窗失败，失败原因为：{}".format(e))

    # 未登录状态，首页点击"未登录"，弹窗提示登录，点击[去登录]按钮跳转到登录页面，返回首页
    # def login_window_go_login(self):
    #     log.info("首页，点击'未登录'，弹窗提示登录，点击[去登录]按钮...")
    #     try:
    #         # 点击首页-未登录
    #         notLogin = self.driver.find_element(*self.notLoginBtn)
    #         notLogin.click()
    #         time.sleep(2)
    #
    #         # 点击登录提示弹窗-[去登陆]按钮
    #         goLogin = self.driver.find_element(*self.goLoginBtn)
    #         goLogin.click()
    #         time.sleep(2)
    #
    #         # 判断是否跳转至登录页面
    #         boo = is_exist_element(self.driver, "获取验证码")
    #         if boo == True:
    #             # 点击返回按钮
    #             ret = self.driver.find_element(*self.returnBtn)
    #             ret.click()
    #             log.info("跳转登录页成功，返回首页...")
    #     except Exception as e:
    #         ScreenShot(self.driver, "跳转登录页error").screen_shot()
    #         log.error("首页，点击'未登录'，弹窗提示登录，点击[去登录]按钮跳转页面失败，失败原因为：{}".format(e))

    # 未登录状态，切换至学院页面
    def switch_page(self):
        log.info("===当前方法：%s，验证未登录状态能否查看学院文章===" % p.get_current_function_name())

        try:
            # 首页切换至学院
            academyElement = self.driver.find_element(*self.academyBtn)
            academyElement.click()
            log.info("切换至学院页")
            time.sleep(1)

            # 点击进入喵星人-入门课堂-养猫准备文章列表页
            feedCatReady = self.driver.find_element(*self.feedCatReadyBtn)
            feedCatReady.click()
            log.info("进入喵星人-养猫准备页面")
            time.sleep(1)

            # 点击进入养猫准备中的文章详情页
            contentElement = self.driver.find_element(*self.contentBtn)
            contentElement.click()
            log.info("进入养猫准备文章详情页面")
            time.sleep(1)

            # 点击文章详情页-分享按钮
            page_click(1340, 160)
            log.info("点击文章详情页面-分享按钮，分享弹窗")
            time.sleep(1)

            # 点击分享弹窗-[取消]按钮
            cancelElement = self.driver.find_element(*self.cancelBtn)
            cancelElement.click()
            log.info("点击分享弹窗-[取消]按钮，弹窗消失")
            time.sleep(1)

            # 点击文章详情页-返回按钮
            page_click(80, 160)
            log.info("点击文章详情页面-返回按钮，返回至文章列表页")
            time.sleep(1)

            # 点击文章列表页-返回按钮
            retElement = self.driver.find_element(*self.returnBtn)
            retElement.click()
            log.info("点击文章列表页-返回按钮，返回至学院页面")
            time.sleep(1)
        except Exception as e:
            ScreenShot(self.driver, e)
            log.error("未登录状态-切换至学院页面出错，错误原因为：{}".format(e))

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(6)
    NoLogin(driver).switch_page()