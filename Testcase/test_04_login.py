#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/05
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseOperate import page_click
from Base.BaseDriver import BaseDriver
from Base.BaseMethod import is_exist_element, is_exist_toast
from Base.BaseScreenShot import ScreenShot

# 验证登录功能
class LoginOut(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录"]')  # 记录页tab
    healthBtn = (By.XPATH, '//android.widget.TextView[@text="健康管理"]')   # 记录页-健康管理
    goLoginBtn = (By.XPATH, '//android.widget.TextView[@text="去登录"]')  # 登录弹窗-[去登录]按钮
    telNoBox = (By.XPATH, '//android.widget.EditText[@text="请输入常用手机号"]') # 手机号输入框
    getCodeBtn = (By.XPATH, '//android.widget.TextView[@text="获取验证码"]')  # 登录页-[获取验证码]按钮
    codeInputBox = (By.XPATH, '//android.widget.EditText[@text="请输入验证码"]')  # 验证码输入框
    loginBtn = (By.XPATH, '//android.widget.TextView[@text="登录" and @index=1]')  # [登录]按钮
    myTab = (By.XPATH, '//android.widget.TextView[@text="我的"]') # 我的tab
    setBtn = (By.XPATH, '//android.widget.TextView[@text="我的" and @index=2]/../android.view.View[@index=1]')    # 我的-设置
    logoutBtn = (By.XPATH, '//android.widget.TextView[@text="退出登录"]')   # 设置-[退出登录]按钮
    sureBtn = (By.XPATH, '//android.widget.TextView[@text="确定"]')   # 设置-退出登录弹窗-[确定]按钮
    passwordLoginBtn = (By.XPATH, '//android.widget.TextView[@text="账号密码登录"]')  # 登录页-账号密码登录
    pwdBox = (By.XPATH, '//android.widget.TextView[@text="密    码"]/../android.widget.EditText') # 账号密码登录页-密码输入框
    weChatBtn = (By.XPATH, '//android.widget.TextView[@text="其他登录方式"]/../android.view.View[@index=5]') # 登录页-微信登录按钮

    telephone = "18768124236"
    password = "******"


    # 进入登录页面
    def access_to_login_page(self):
        # 未登录状态切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("未登录状态，切换至记录页，准备进入登录页面进行登录测试")
        time.sleep(1)

        # 点击健康管理，弹窗提示去登录页面
        health = self.driver.find_element(*self.healthBtn)
        health.click()
        log.info("点击记录页-健康管理，弹窗提示登录")
        time.sleep(1)

        # 跳转至登录页面
        goLogin = self.driver.find_element(*self.goLoginBtn)
        goLogin.click()
        log.info("跳转至登录页面")
        time.sleep(1)
        # boo = is_exist_element(self.driver, "获取验证码")
        # if boo == True:
        #     log.info("点击[去登录]，跳转至登录页面成功！")

    # 验证码登录
    def code_login(self):
        log.info("===当前方法：%s，验证码登录功能验证===" % p.get_current_function_name())

        # 进入登录页面
        self.access_to_login_page()

        # 输入手机号
        telNo = self.driver.find_element(*self.telNoBox)
        telNo.send_keys(self.telephone)
        log.info("输入手机号：{}".format(self.telephone))

        # 因为输入手机号会调出键盘，点击获取验证码之前需点击屏幕任意位置让键盘隐藏，然后才能点击[获取验证码]按钮
        page_click(700, 350)
        log.info("隐藏键盘")
        time.sleep(1)

        # 点击[获取验证码]按钮
        getCode = self.driver.find_element(*self.getCodeBtn)
        getCode.click()
        log.info("点击获取验证码")
        time.sleep(1)

        # 手动输入验证码
        code = input("请输入验证码：")
        codeInput = self.driver.find_element(*self.codeInputBox)
        codeInput.send_keys(code)
        log.info("输入的验证码是：{}".format(code))
        time.sleep(1)

        # 隐藏键盘
        page_click(700, 350)
        time.sleep(1)

        # 点击登录按钮
        login = self.driver.find_element(*self.loginBtn)
        login.click()
        log.info("点击登录按钮")
        time.sleep(5)
        # 判断是否登录成功
        boo = is_exist_element(self.driver, "未登录")
        if boo == False:
            log.info("验证码登录成功")
            # 退出登录
            self.logout()
        else:
            log.error("验证码登录失败，错误页面截图！！！")
            ScreenShot(self.driver, "验证码登录失败").screen_shot()

    # 退出登录
    def logout(self):
        # 切换至"我的"tab页
        log.info("进行退出登录操作")
        my = self.driver.find_element(*self.myTab)
        my.click()
        log.info("切换至'我的'页面")
        time.sleep(2)

        # 点击设置按钮
        set = self.driver.find_element(*self.setBtn)
        set.click()
        log.info("点击设置，进入设置页面")
        time.sleep(2)

        # 设置页面点击[退出登录]按钮
        logout = self.driver.find_element(*self.logoutBtn)
        logout.click()
        log.info("点击[退出登录]-[确定]")
        time.sleep(2)

        # 点击确定
        sure = self.driver.find_element(*self.sureBtn)
        sure.click()
        time.sleep(2)

        # 切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("切换至记录页")
        time.sleep(1)

        # 判断退出登录是否成功
        boo = is_exist_element(self.driver, "未登录")
        if boo == True:
            log.info("退出登录成功！")

    # 密码登录
    def password_login(self):
        log.info("===当前方法：%s，验证账号密码登录功能===" % p.get_current_function_name())

        # 进入登录页面
        self.access_to_login_page()

        # 登录页点击[账号密码登录]按钮，进入账号密码登录页
        passwordLogin = self.driver.find_element(*self.passwordLoginBtn)
        passwordLogin.click()
        log.info("点击[账号密码登录]按钮，进入账号密码登录页")
        time.sleep(1)

        # 输入手机号
        telNo = self.driver.find_element(*self.telNoBox)
        telNo.send_keys(self.telephone)
        log.info("输入手机号：{}".format(self.telephone))

        # 输入密码
        pwd = self.driver.find_element(*self.pwdBox)
        pwd.send_keys(self.password)
        log.info("输入密码：{}".format(self.password))
        time.sleep(1)

        # 点击登录按钮
        login = self.driver.find_element(*self.loginBtn)
        login.click()
        log.info("点击登录按钮")
        time.sleep(2)

        # 判断是否登录成功
        boo = is_exist_element(self.driver, "未登录")
        if boo == False:
            log.info("密码登录成功！")
            # 退出登录
            # self.logout()
        else:
            log.info("密码登录失败，错误页面截图！！！")
            ScreenShot(self.driver, "密码登录失败").screen_shot()

    # 微信登录
    def weixin_login(self):
        log.info("===当前方法：%s，验证微信登录功能验证" % p.get_current_function_name())

        # 进入登录页面
        self.access_to_login_page()

        # 点击微信登录按钮
        weChat = self.driver.find_element(*self.weChatBtn)
        weChat.click()
        log.info("点击微信登录按钮")
        time.sleep(2)

        # 使用uiautomator2检测toast
        # toa = is_exist_toast(self.driver, "检测到您没有安装微信")
        # if toa == True:
        #     log.info("该手机没有安装微信...")
        # else:
        #     time.sleep(2)
        #     boo = is_exist_element(self.driver, "登录微信")
        #     if boo == True:
        #         # 点击微信登录页返回按钮，返回至登录页面
        #         page_click(60, 160)
        #         log.info("该手机未登录微信，跳转至微信登录页面...")
        #     else:
        #         boo1 = is_exist_element(self.driver, "未登录")
        #         boo2 = is_exist_element(self.driver, "允许")
        #         if boo1 == False and boo2 == False:
        #             log.info("微信登录成功！")
        #             # 退出登录
        #             self.logout()
        #         elif boo1 == False and boo2 == True:
        #             log.info("需要绑定微信，页面跳转至微信用户信息授权页面...")
        #             pass
        #         else:
        #             # 错误截图
        #             ScreenShot(self.driver, "微信登录错误").screen_shot()
        #             log.error("微信登录出错，已截图！！！")

        boo = is_exist_element(self.driver, "未登录")
        if boo == True:
            ScreenShot(self.driver, "微信登录失败")
            log.error("微信登录失败，失败原因请查看截图！")
        else:
            boo = is_exist_element(self.driver, "登录微信")
            if boo == True:
                # 点击微信登录页返回按钮，返回至登录页面
                page_click(60, 160)
                log.info("该手机未登录微信，跳转至微信登录页面")
            else:
                boo1 = is_exist_element(self.driver, "未登录")
                boo2 = is_exist_element(self.driver, "允许")
                if boo1 == False and boo2 == False:
                    log.info("微信登录成功！")
                    # 退出登录
                    self.logout()
                elif boo1 == False and boo2 == True:
                    log.info("需要绑定微信，页面跳转至微信用户信息授权页面")
                    pass
                else:
                    # 错误截图
                    ScreenShot(self.driver, "微信登录错误").screen_shot()
                    log.error("微信登录出错，已截图！！！")


if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    loginOut = LoginOut(driver)
    loginOut.code_login()