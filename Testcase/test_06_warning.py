#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/20
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver
from Base.BaseOperate import BaseOperate
from Base.BaseMethod import is_exist_element
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

# 提醒吧
class WarningBar(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录" and @index=1]/..')  # 发现
    warningBtn = (By.XPATH, '//android.widget.TextView[@text="提醒吧"]')   # 记录页-提醒吧
    addBtn = (By.XPATH, '//android.widget.TextView[@text="添加"]')    # 提醒吧-添加按钮
    addWarningTitle = (By.XPATH, '//android.widget.TextView[@text="添加提醒"]') # 添加提醒列表页标题
    userDefinedBtn = (By.XPATH, '//android.widget.TextView[@text="自定义"]')   # 添加提醒列表页-自定义按钮
    contentBox = (By.XPATH, '//android.widget.EditText[@text="请输入内容"]') # 新增提醒-内容输入框
    noteBox = (By.XPATH, '//android.widget.EditText[@text="请输入备注"]') # 新增提醒-备注输入框
    warningTimeBtn = (By.XPATH, '//android.widget.TextView[@text="请选择时间"]') # 新增提醒-提醒时间

    t_content = '777'
    note_content = '888'

    timeWindow = (By.XPATH, '//android.widget.LinearLayout[@index=0]')  # 新增提醒-时间弹窗
    daytime = (By.ID, 'com.pets.mhcw:id/dpv_day')   # 时间弹窗-日期滑动
    confirmBtn = (By.ID, 'com.pets.mhcw:id/tv_confirm')    # 时间弹窗-确定按钮
    saveBtn = (By.XPATH, '//android.widget.TextView[@text="保存"]')   # 新增提醒-保存按钮

    newWarningBtn = (By.XPATH, '//android.widget.TextView[@text={}]'.format(t_content)) # 提醒吧页面-新增提醒项
    finishBtn = (By.XPATH, '//android.widget.TextView[@text="完成"]') # 提醒详情页-完成按钮

    new = (By.XPATH, '//android.widget.TextView[@text={}]/../../../..'.format(t_content))   # 提醒吧页面-新增提醒项顶层元素
    finished = (By.XPATH, '//android.widget.TextView[@text="已完成"]/..') # 提醒吧页面-已完成元素
    deleteBtn = (By.XPATH, '//android.widget.TextView[@text={}]/../../../../android.view.View[@index=1]'.format(t_content))  # 提醒吧页面-提醒项删除按钮

    backBtn = (By.XPATH, '//android.widget.TextView[@text="提醒吧" and @index=2]/../android.view.View[@index=1]')  # 提醒吧页面-返回按钮

    # 新增提醒
    def add_warning(self):
        log.info("===当前方法：%s，验证提醒吧-新增提醒功能===" % p.get_current_function_name())

        # 首页切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("首页跳转至发现页")
        time.sleep(1)

        # 记录页进入提醒吧
        warningElement = self.driver.find_element(*self.warningBtn)
        warningElement.click()
        log.info("进入提醒吧页面")
        time.sleep(1)

        # 点击添加按钮
        addElement = self.driver.find_element(*self.addBtn)
        addElement.click()
        log.info("进入提醒吧-点击添加按钮判断是否有添加提醒页")
        time.sleep(1)

        # 判断是否有添加提醒页(宠物品种为其他则有添加提醒页)
        try:
            self.driver.find_element(*self.addWarningTitle)
            # 提醒类表页上滑页面，点击自定义进入新增提醒页
            BaseOperate(self.driver).swipeUp()
            time.sleep(1)
            userDefinedEle = self.driver.find_element(*self.userDefinedBtn)
            userDefinedEle.click()
            log.info("有添加提醒页，点击自定义进入新增提醒页")
            time.sleep(1)
        except NoSuchElementException:
            log.info("无添加提醒页面")
            pass

        # 输入内容
        contentElement = self.driver.find_element(*self.contentBox)
        contentElement.send_keys(self.t_content)
        # 输入备注
        noteElement = self.driver.find_element(*self.noteBox)
        noteElement.send_keys(self.note_content)
        log.info("内容输入：{}，时间输入：{}".format(self.t_content, self.note_content))

        # 设置提醒时间
        warningTimeElement = self.driver.find_element(*self.warningTimeBtn)
        warningTimeElement.click()
        log.info("设置提醒时间")
        # 获取弹窗左上角纵坐标
        timeWindowElement = self.driver.find_element(*self.timeWindow)
        w_point = timeWindowElement.location
        w_y = w_point['y']
        # 获取日期时间元素坐标
        daytimeElement = self.driver.find_element(*self.daytime)
        d_point = daytimeElement.location
        d_x = d_point['x']
        d_y = d_point['y']
        # 滑动后的坐标
        x = d_x
        y = (d_y + w_y)/2
        # 滑动日期时间元素
        TouchAction(self.driver).long_press(daytimeElement).move_to(x=x, y=y).release().perform()
        time.sleep(1)
        # 点击确定
        confirmElement = self.driver.find_element(*self.confirmBtn)
        confirmElement.click()
        time.sleep(1)

        # 保存
        saveElement = self.driver.find_element(*self.saveBtn)
        saveElement.click()
        time.sleep(2)

        # 判断新增提醒是否成功
        boo = is_exist_element(self.driver, self.t_content)
        if boo == True:
            log.info("新增提醒成功！")
        else:
            log.error("新增提示失败！")

    # 提醒完成
    def finished_warning(self):
        log.info("===当前方法：%s，验证提醒完成功能===" % p.get_current_function_name())
        # 获取点击提醒完成之前新增提醒元素的index
        # finishedElement = self.driver.find_element(*self.new)
        # pre_index = finishedElement.get_attribute('index')

        # 提醒吧页面点击刚刚新增的提醒
        newWarningElement = self.driver.find_element(*self.newWarningBtn)
        newWarningElement.click()
        time.sleep(1)

        # 提醒详情页点击完成按钮
        finishElement = self.driver.find_element(*self.finishBtn)
        finishElement.click()
        log.info("点击完成按钮")
        time.sleep(2)

        # 获取点击提醒完成之后新增提醒元素的index
        # finishedElement = self.driver.find_element(*self.new)
        # la_index = finishedElement.get_attribute('index')
        #
        # # 通过判断新增提醒元素点击完成前后index大小的比较，来判断该提醒项点击完成后是否跳至已完成
        # if pre_index < la_index:
        #     log.info("新增提醒项已完成！")
        # else:
        #     log.error("新增提醒项点击完成出错，未完成！")

    # 删除已完成的提醒
    def delete_warning(self):
        log.info("===当前方法：%s，验证删除提醒项功能===" % p.get_current_function_name())

        # 获取屏幕宽、高
        w_x, w_y = BaseOperate(self.driver).get_size()
        # 获取新增提醒项标题元素左上角坐标
        try:
            newWarningElement = self.driver.find_element(*self.newWarningBtn)
            point = newWarningElement.location
        except NoSuchElementException:
            # 没有找到该元素则上滑页面
            BaseOperate(self.driver).swipeUp()
            time.sleep(1)
            newWarningElement = self.driver.find_element(*self.newWarningBtn)
            point = newWarningElement.location
        p_x = point['x']
        p_y = point['y']
        # 起点坐标
        start_x = w_x*0.5
        start_y = p_y
        # 移动后坐标
        end_x = p_x
        end_y = p_y
        # 向左滑动新增提醒项
        TouchAction(self.driver).long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()
        log.info("向左滑动新增提醒项")
        time.sleep(1)

        # 点击删除按钮
        deleteElement = self.driver.find_element(*self.deleteBtn)
        deleteElement.click()
        log.info("点击删除")
        time.sleep(1)

        # 判断是否删除成功
        boo = is_exist_element(self.driver, self.t_content)
        if boo == False:
            log.info("提醒吧-新增提醒项删除成功！")
        else:
            log.error("提醒吧-新增提醒项删除失败！")

        # 返回记录页
        backElement = self.driver.find_element(*self.backBtn)
        backElement.click()
        log.info("提醒吧页面返回至记录页")
        time.sleep(1)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    warningBar = WarningBar(driver)
    warningBar.add_warning()
    # time.sleep(1)
    # warningBar.finished_warning()
    # time.sleep(1)
    # warningBar.delete_warning()