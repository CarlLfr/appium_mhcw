#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/09
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from Base.BaseMethod import is_exist_element
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseScreenShot import ScreenShot
from Base.BaseDriver import BaseDriver
from Base.BaseOperate import BaseOperate

# 验证注册功能
class Register(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录"]')  # 记录页tab
    healthBtn = (By.XPATH, '//android.widget.TextView[@text="健康管理"]')  # 记录页-健康管理
    goLoginBtn = (By.XPATH, '//android.widget.TextView[@text="去登录"]')  # 登录弹窗-[去登录]按钮
    regBtn = (By.XPATH, '//android.widget.TextView[@text="注册"]')   # 登录页-注册按钮
    returnBtn = (By.XPATH, '//android.view.View[@index=1]')  # 登录页-[返回]按钮
    agreeBtn = (By.XPATH, '//android.widget.TextView[@text="同意"]')  # 注册页提示弹窗-[同意]按钮
    disagreeBtn = (By.XPATH, '//android.widget.TextView[@text="不同意"]')  # 注册页提示弹窗-[不同意]按钮
    protocolBtn = (By.XPATH, '//android.widget.TextView[@text="短信验证码收不到？试试语音验证"]/../android.widget.TextView[@index=8]') # 用户注册及隐私协议
    retBtn = (By.XPATH, '//android.widget.TextView[@text="用户注册及隐私声明" and @index=2]/../android.view.View[@index=1]')    # 用户注册及隐私协议页-返回按钮
    noPetBtn = (By.XPATH, '//android.widget.TextView[@text="未添加宠物" and @index=1]')  # 注册成功后首页-未添加宠物按钮
    goAddBtn = (By.XPATH, '//android.widget.TextView[@text="去添加"]') # 注册成功-未添加宠物-提示添加宠物弹窗-[去添加]按钮
    cancelBtn = (By.XPATH, '//android.widget.TextView[@text="取消"]') # 注册成功-未添加宠物-提示添加宠物弹窗-[取消]按钮

    telBox = (By.XPATH, '//android.widget.EditText[@text="请输入常用手机号"]')  # 注册页-手机号输入框
    codeBtn = (By.XPATH, '//android.widget.TextView[@text="获取验证码"]')    # 注册页-获取验证码
    codeBox = (By.XPATH, '//android.widget.EditText[@text="请输入验证码"]')    # 注册页-验证码输入框
    pwdBox = (By.XPATH, '//android.widget.TextView[@text="密    码"]/../android.widget.EditText')  # 注册页-密码输入框
    registerBtn = (By.XPATH, '//android.widget.TextView[@text="注册" and @index=1]')  # 注册页-[注册]按钮

    clockInBtn = (By.XPATH, '//android.widget.TextView[@text="日常打卡"]')  # 注册-首页-日常打卡按钮
    catBtn = (By.XPATH, '//android.widget.TextView[@text="喵星人"]')   # 宠物品种页-喵星人
    petNameBox = (By.XPATH, '//android.widget.EditText[@text="输入宠物昵称"]')    # 添加宠物页-昵称输入框
    sexBtn = (By.XPATH, '//android.widget.TextView[@text="选择宠物性别"]')    # 添加宠物页-性别选择
    maleBtn = (By.XPATH, '//android.widget.TextView[@text="公"]')    # 添加宠物页-性别-公
    saveBtn = (By.XPATH, '//android.widget.TextView[@text="保存"]')   # 添加宠物页-保存按钮


    oldTelephone = '18768124236'    # 已存在的用户
    rightPwd = "111111"
    wrongPwd = "11111"
    petname = "奥特曼"


    # 进入注册页
    def get_in_register(self):
        # 进入登录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("未登录状态，切换至记录页，准备进入登录页面进行登录测试")
        time.sleep(1)

        # 点击健康管理，弹窗提示去登录页面
        healthElement = self.driver.find_element(*self.healthBtn)
        healthElement.click()
        log.info("点击记录页-健康管理，弹窗提示登录")
        time.sleep(1)

        # 跳转至登录页面
        goLoginEle = self.driver.find_element(*self.goLoginBtn)
        goLoginEle.click()
        time.sleep(1)
        boo = is_exist_element(self.driver, "获取验证码")
        if boo == True:
            log.info("点击[去登录]，跳转至登录页面成功！")

        # 点击登录页[注册]按钮
        regElement = self.driver.find_element(*self.regBtn)
        regElement.click()
        log.info("点击登录页[注册]按钮，进入注册页面")
        time.sleep(1)

        # 点击弹窗同意按钮
        agreeElement = self.driver.find_element(*self.agreeBtn)
        agreeElement.click()
        log.info("点击注册页提示弹窗-[同意]按钮，弹窗消失")
        time.sleep(1)

    # 进入《用户注册及隐私协议》页
    def get_in_protocol(self):
        log.info("===当前方法：%s，验证能否查看《用户注册及隐私协议》===" % p.get_current_function_name())

        # 进入注册页
        self.get_in_register()

        # 点击《用户注册及隐私协议》
        protocol = self.driver.find_element(*self.protocolBtn)
        protocol.click()
        time.sleep(1)
        # 判断是否跳转至用户注册及隐私协议页
        boo1 = is_exist_element(self.driver, "请输入常用手机号")
        # print(boo1)
        boo2 = is_exist_element(self.driver, "用户注册及隐私声明")
        # print(boo2)
        if boo1 == False and boo2 == True:
            log.info("进入《用户注册及隐私协议》页面成功！")
            # 点击返回按钮
            ret = self.driver.find_element(*self.retBtn)
            ret.click()
            log.info("点击返回至注册页面！")
            time.sleep(1)
        else:
            ScreenShot(self.driver, "跳转用户注册及隐私协议页面失败")
            log.error("跳转用户注册及隐私协议页面失败，错误截图！")

    # 输入已经注册过的手机号进行注册
    def old_user_register(self):
        log.info("===当前方法：%s，验证已注册过的手机号进行注册===" % p.get_current_function_name())

        # 进入注册页
        # self.get_in_register()

        # 输入已注册用户手机号，点击获取验证码
        telElement = self.driver.find_element(*self.telBox)
        telElement.send_keys(self.oldTelephone)

        codeElement = self.driver.find_element(*self.codeBtn)
        codeElement.click()
        log.info("输入已注册用户手机号，点击获取验证码")
        time.sleep(1)

        # 已注册用户点击获取验证码 提示并跳转至登录页
        boo = is_exist_element(self.driver, "账号密码登录")
        if boo == True:
            log.info("跳转至登录页面，点击返回至记录页")
            ret = self.driver.find_element(*self.returnBtn)
            ret.click()
            time.sleep(1)
            # log.info("跳转至登录页面，点击[注册]按钮再次跳转至注册页面...")
            # # 点击登录页[注册]按钮
            # reg = self.driver.find_element(*self.regBtn)
            # reg.click()
            # log.info("点击登录页[注册]按钮，进入注册页面...")
            # time.sleep(1)
            #
            # # 点击弹窗同意按钮
            # agree = self.driver.find_element(*self.agreeBtn)
            # agree.click()
            # log.info("点击注册页提示弹窗-[同意]按钮，弹窗消失...")
            # time.sleep(1)
        else:
            ScreenShot(self.driver, "已注册用户注册页跳转至登录页失败")
            log.error("已注册用户注册页跳转至登录页失败！！！")

    # 输入未注册过的手机号进行注册，并添加宠物
    def new_register(self):
        log.info("===当前方法：%s，验证未注册过的手机号进行注册，并添加宠物功能" % p.get_current_function_name())

        # 进入注册页
        # self.get_in_register()

        telElement = self.driver.find_element(*self.telBox)
        newTelephone = input("请输入未注册过的手机号码：")
        telElement.send_keys(newTelephone)

        # 点击获取验证码
        codeElement = self.driver.find_element(*self.codeBtn)
        codeElement.click()
        log.info("输入未注册过的手机号，点击获取验证码")
        time.sleep(2)

        # 判断验证码是否获取成功
        boo1 = is_exist_element(self.driver, "56s")
        boo2 = is_exist_element(self.driver, "55s")
        boo3 = is_exist_element(self.driver, "54s")
        if boo1 == True or boo2 == True or boo3 == True:
            log.info("获取验证码成功！")
            code = input("请输入验证码：")
            cod = self.driver.find_element(*self.codeBox)
            cod.send_keys(code)

            # 输入密码
            pwd = self.driver.find_element(*self.pwdBox)
            pwd.send_keys(self.rightPwd)
            time.sleep(1)

            # 点击登录按钮
            register = self.driver.find_element(*self.registerBtn)
            register.click()
            time.sleep(2)

            # 判断是否注册成功
            boo4 = is_exist_element(self.driver, "未添加宠物")
            if boo4 == True:
                log.info("注册成功！")
                # 添加宠物
                self.add_pets()
            else:
                ScreenShot(self.driver, "注册失败").screen_shot()
                log.error("注册失败！！！")
        else:
            ScreenShot(self.driver, "注册时获取验证码失败").screen_shot()
            log.error("注册时获取验证码失败！！！")

    # 新注册登录未添加宠物，去添加宠物
    def add_pets(self):
        # 点击日常打卡-去添加
        clockElement = self.driver.find_element(*self.clockInBtn)
        clockElement.click()
        goAdd = self.driver.find_element(*self.goAddBtn)
        goAdd.click()
        log.info("新注册用户，点击首页日常打卡-去添加，跳转至选择宠物品种页")
        time.sleep(1)

        # 点击喵星人
        catElement = self.driver.find_element(*self.catBtn)
        catElement.click()
        log.info("宠物品种页点击喵星人，跳转至添加页面")
        time.sleep(1)

        # 输入昵称
        petName = self.driver.find_element(*self.petNameBox)
        petName.send_keys(self.petname)
        # 选择性别
        sex = self.driver.find_element(*self.sexBtn)
        sex.click()
        male = self.driver.find_element(*self.maleBtn)
        male.click()

        # 页面上滑、点击保存按钮
        BaseOperate(self.driver).swipeUp()
        save = self.driver.find_element(*self.saveBtn)
        save.click()
        time.sleep(2)

        # 判断宠物添加是否成功
        boo = is_exist_element(self.driver, self.petname)
        if boo == True:
            log.info("宠物添加成功，跳转至首页！")
        else:
            ScreenShot(self.driver, "添加宠物跳转至首页失败").screen_shot()
            log.error("添加宠物跳转至首页失败！！！")


if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    register = Register(driver)
    register.get_in_protocol()
    register.old_user_register()