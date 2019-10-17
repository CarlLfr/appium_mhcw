#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/09/19
# @Author  : Liufeiru

import time
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver
from Base.BaseOperate import BaseOperate, swipe_element_left
from Base.BaseMethod import is_exist_element
from Base.BaseScreenShot import ScreenShot
from selenium.common.exceptions import NoSuchElementException

# 日常打卡
class DailyClick(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录"]')  # 记录页tab
    dailyBtn = (By.XPATH, '//android.widget.TextView[@text="日常打卡"]')    # 记录页-日常打卡选项
    addBtn = (By.XPATH, '//android.widget.TextView[@text="添加"]')    # 日常打卡页面-添加按钮
    dailyItemBox = (By.XPATH, '//android.widget.EditText[@text="请输入事项"]')   # 日常打卡添加页面-日常事项输入框
    encourageBox = (By.XPATH, '//android.widget.EditText[@text="请输入鼓励语"]')   # 日常打卡添加页面-鼓励语输入框
    saveBtn = (By.XPATH, '//android.widget.TextView[@text="保存"]')   # 日常打卡添加页面-保存按钮
    dailyItem_content = '995'   # 日常事项输入内容
    encourage_content = '996'   # 鼓励语

    eatBtn = (By.XPATH, '//android.widget.TextView[@text="吃饭"]/../../android.view.View[@index=2]')  # 日常打卡页面-吃饭
    excreteBtn = (By.XPATH, '//android.widget.TextView[@text="排泄"]/../../android.view.View[@index=2]')  # 日常打卡页面-排泄
    newBtn = (By.XPATH, '//android.widget.TextView[@text={}]/../../android.view.View[@index=2]'.format(dailyItem_content))  # 日常打卡页面-新增事项
    backBtn = (By.XPATH, '//android.widget.TextView[@text="日常打卡" and @index=2]/../android.view.View[@index=1]')    # 日常打卡页面-返回按钮

    deleteBtn = (By.XPATH, '//android.widget.TextView[@text={}]/../../../android.view.View[@index=1]'.format(dailyItem_content))    # 日常打卡页-新增选项-删除按钮

    # 添加日常事项
    def add_item(self):
        log.info("===当前方法：%s，验证日常打卡-添加功能===" % p.get_current_function_name())

        # 切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("切换至记录页")
        time.sleep(1)

        # 记录页点击日常打卡进入页面
        daily = self.driver.find_element(*self.dailyBtn)
        daily.click()
        log.info("进入日常打卡页面")
        time.sleep(0.5)

        # 日常打卡页面有新手引导则点击跳过
        da = self.driver.find_element(*self.dailyBtn)
        da.click()
        time.sleep(0.5)
        da.click()
        time.sleep(0.5)

        # 添加，进入添加页面
        try:
            addElement = self.driver.find_element(*self.addBtn)
            addElement.click()
        except NoSuchElementException:
            # 没有找到添加按钮元素则上滑页面，再点击
            BaseOperate(self.driver).swipeUp()
            time.sleep(1)
            self.driver.find_element(*self.addBtn).click()
        log.info("进入添加页面")
        time.sleep(1)

        # 日常事项输入，鼓励语输入
        dailyItem = self.driver.find_element(*self.dailyItemBox)
        dailyItem.send_keys(self.dailyItem_content)

        encourage = self.driver.find_element(*self.encourageBox)
        encourage.send_keys(self.encourage_content)
        log.info("日常事项输入：{}，鼓励语输入：{}".format(self.dailyItem_content, self.encourage_content))
        time.sleep(1)

        # 点击保存
        save = self.driver.find_element(*self.saveBtn)
        save.click()
        time.sleep(1)

        # 判断是否添加成功
        boo = is_exist_element(self.driver, self.dailyItem_content)
        if boo == True:
            log.info("添加日常事项成功！")
        else:
            log.error("日常打卡添加失败！")

    # 打卡
    def daily_click(self):
        log.info("===当前方法：%s，验证日常打卡-打卡功能===" % p.get_current_function_name())

        # 点击吃饭
        eat = self.driver.find_element(*self.eatBtn)
        eat.click()
        log.info("点击吃饭")
        time.sleep(1)

        # 点击排泄
        excrete = self.driver.find_element(*self.excreteBtn)
        excrete.click()
        log.info("点击排泄")
        time.sleep(1)

        # 点击新增事项
        try:
            newElement = self.driver.find_element(*self.newBtn)
            newElement.click()
        except NoSuchElementException:
            BaseOperate(self.driver).swipeUp()
            self.driver.find_element(*self.newBtn).click()
        log.info("点击新增事项")

        # 点击返回按钮
        back = self.driver.find_element(*self.backBtn)
        back.click()
        log.info("日常打卡页面添加打卡后，返回记录页")
        time.sleep(2)

        # 验证是否打卡成功
        boo = is_exist_element(self.driver, "{}：{}".format(self.dailyItem_content, self.encourage_content))
        if boo == True:
            log.info("日常打卡成功！")
            pass
        else:
            log.error("日常打卡失败！")

    # 删除日常事项
    def delete_item(self):
        log.info("===当前方法：%s，验证日常打卡-删除日常事项功能===" % p.get_current_function_name())

        global newElement
        # 记录页点击日常打卡进入页面
        daily = self.driver.find_element(*self.dailyBtn)
        daily.click()
        log.info("进入日常打卡页面")
        time.sleep(1)

        # 新增选项左滑
        try:
            newElement = self.driver.find_element(*self.newBtn)
        except NoSuchElementException:
            BaseOperate(self.driver).swipeUp()
        finally:
            log.info("开始删除{}选项".format(self.dailyItem_content))
            swipe_element_left(self.driver, newElement)
            time.sleep(1)

            # 点击删除按钮
            deleteElement = self.driver.find_element(*self.deleteBtn)
            deleteElement.click()
            time.sleep(2)

        # 判断是否删除成功
        boo = is_exist_element(self.driver, self.dailyItem_content)
        if boo == False:
            log.info("日常打卡新增项删除成功！")
        else:
            log.error("日常打卡新增项删除失败！")

        # 返回记录页
        backElement = self.driver.find_element(*self.backBtn)
        backElement.click()
        log.info("由日常打卡页面返回至记录页")
        time.sleep(1)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    dailyClick = DailyClick(driver)
    dailyClick.add_item()
    dailyClick.daily_click()
    dailyClick.delete_item()