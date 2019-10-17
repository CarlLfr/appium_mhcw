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
from Base.BaseMethod import is_exist_element
from Base.BaseOperate import BaseOperate, swipe_element_left
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

# 健康管理
class HealthManagement(BaseView):
    healthBtn = (By.XPATH, '//android.widget.TextView[@text="健康管理"]')   # 首页-健康管理
    addBtn = (By.XPATH, '//android.widget.TextView[@text="添加"]')    # 健康管理-添加按钮

    clinicTimeBtn = (By.XPATH, '//android.widget.TextView[@text="请选择就诊时间"]')    # 新增-就诊时间选择
    timeWindow = (By.XPATH, '//android.widget.LinearLayout[@index=0]')  # 时间选择弹窗
    daytime = (By.ID, 'com.pets.mhcw:id/dpv_day') # 时间选择弹窗-日期选择
    confirmBtn = (By.ID, 'com.pets.mhcw:id/tv_confirm') # 时间选择弹窗-确定按钮

    hospitalBox = (By.XPATH, '//android.widget.EditText[@text="请输入就诊医院"]')  # 新增-就诊医院输入框
    resultBox = (By.XPATH, '//android.widget.EditText[@text="请输入结果"]')  # 新增-诊断结果输入框
    illStateBox = (By.XPATH, '//android.widget.EditText[@text="请描述宠物病情"]')  # 新增-请描述宠物病情输入框
    saveBtn = (By.XPATH, '//android.widget.TextView[@text="保存"]')   # 新增-保存按钮
    illStateText = (By.XPATH, '//android.widget.TextView[@text="病情描述"]')  # 新增-病情描述展示
    hos_content = '666'
    res_content = '250'
    state_content = '500'
    change_state_content = '555'

    newItem = (By.XPATH, '//android.widget.TextView[@text="医院：{}"]'.format(hos_content))    # 健康管理页-新增项医院名称
    newIllState = (By.XPATH, '//android.view.View[@index=4]/android.widget.EditText[@index=0]')  # 修改时进入新增页面-请描述宠物病情输入框

    deleteBtn = (By.XPATH, '//android.widget.TextView[@text="删除"]') # 管理项详情页-删除按钮
    sureBtn = (By.XPATH, '//android.widget.TextView[@text="确定"]') # 管理项详情页-点击删除弹窗-确定按钮

    backBtn = (By.XPATH, '//android.widget.TextView[@text="健康管理" and @index=2]/../android.view.View[@index=1]') # 健康管理页面-返回按钮

    # 新增
    def add_health_item(self):
        log.info("===当前方法：%s，验证健康管理新增功能===" % p.get_current_function_name())

        # 首页进入健康管理
        healthElement = self.driver.find_element(*self.healthBtn)
        healthElement.click()
        log.info("进入健康管理页面")
        time.sleep(1)

        # 点击添加按钮
        addElement = self.driver.find_element(*self.addBtn)
        addElement.click()
        log.info("进入健康管理-添加页面")
        time.sleep(2)

        # 时间选择
        clinicTimeElement = self.driver.find_element(*self.clinicTimeBtn)
        clinicTimeElement.click()
        time.sleep(1)
        log.info("设置时间")
        # 获取时间选择弹窗左上角纵坐标
        timeWindowElement = self.driver.find_element(*self.timeWindow)
        w_point = timeWindowElement.location
        w_y = w_point['y']
        # 获取日期选择元素左上角坐标
        daytimeElement = self.driver.find_element(*self.daytime)
        d_point = daytimeElement.location
        d_x = d_point['x']
        d_y = d_point['y']
        x = d_x
        y = d_y + (d_y - w_y)*2
        TouchAction(self.driver).long_press(daytimeElement).move_to(x=x, y=y).release().perform()
        time.sleep(1)
        # 点击确定
        confirmElement = self.driver.find_element(*self.confirmBtn)
        confirmElement.click()
        time.sleep(1)

        # 输入医院
        hospitalElement = self.driver.find_element(*self.hospitalBox)
        hospitalElement.send_keys(self.hos_content)
        time.sleep(0.5)
        # 输入诊断结果
        resultElement = self.driver.find_element(*self.resultBox)
        resultElement.send_keys(self.res_content)
        time.sleep(0.5)
        # 输入病情描述
        illStateElement = self.driver.find_element(*self.illStateBox)
        illStateElement.send_keys(self.state_content)
        log.info("医院输入：{}，诊断结果输入：{}，病情描述输入：{}".format(self.hos_content, self.res_content, self.state_content))
        time.sleep(0.5)

        # 点击保存（先点击病情描述）
        illTextElement = self.driver.find_element(*self.illStateText)
        illTextElement.click()
        time.sleep(1)
        saveElement = self.driver.find_element(*self.saveBtn)
        saveElement.click()
        time.sleep(1)

        # 判断是否新增成功
        boo = is_exist_element(self.driver, "医院：{}".format(self.hos_content))
        if boo == True:
            log.info("新增健康管理成功！")
        else:
            log.error("新增健康管理失败！")

    # 修改
    def change_health_item(self):
        log.info("===当前方法：%s，验证修改健康管理项功能===" % p.get_current_function_name())

        # 进入新增的管理项详情页
        newItemElement = self.driver.find_element(*self.newItem)
        newItemElement.click()
        log.info("进入管理项（医院为：{}）详情页".format(self.hos_content))
        time.sleep(1)

        # 清除之前的病情描述，重新输入
        newIllStateElement = self.driver.find_element(*self.newIllState)
        newIllStateElement.clear()
        newIllStateElement.send_keys(self.change_state_content)
        log.info("清除之前的病情描述，重新输入：{}".format(self.change_state_content))

        # 点击保存（先点击病情描述）
        illTextElement = self.driver.find_element(*self.illStateText)
        illTextElement.click()
        time.sleep(1)
        saveElement = self.driver.find_element(*self.saveBtn)
        saveElement.click()
        time.sleep(1)

        # 判断是否修改成功
        boo = is_exist_element(self.driver, "病情描述：{}".format(self.change_state_content))
        if boo == True:
            log.info("修改健康管理项成功！")
        else:
            log.info("修改健康管理项失败！")

    # 删除
    def delete_health_item(self):
        log.info("===当前方法：%s，验证删除健康管理项功能===" % p.get_current_function_name())

        # 进入新增的管理项
        newItemElement = self.driver.find_element(*self.newItem)
        newItemElement.click()
        log.info("进入管理项（医院为：{}）详情页".format(self.hos_content))
        time.sleep(1)

        # 点击删除按钮
        deleteElement = self.driver.find_element(*self.deleteBtn)
        deleteElement.click()
        time.sleep(1)

        # 点击确定
        sureElement = self.driver.find_element(*self.sureBtn)
        sureElement.click()
        log.info("点击确定删除")
        time.sleep(2)

        # 判断是否删除成功
        boo = is_exist_element(self.driver, "病情描述：{}".format(self.change_state_content))
        if boo == True:
            log.info("删除健康管理项成功！")
        else:
            log.info("删除健康管理项失败！")

        # 返回记录页
        backElement = self.driver.find_element(*self.backBtn)
        backElement.click()
        log.info("由健康管理页面跳转至记录页")
        time.sleep(1)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    healthManagement = HealthManagement(driver)
    healthManagement.add_health_item()
    # healthManagement.change_health_item()
    # healthManagement.delete_health_item()