#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/10/08
# @Author  : Liufeiru

import time
import re
from Base.BaseView import BaseView
from selenium.webdriver.common.by import By
from Base.BaseLog import log
from Base.BaseTools import p
from Base.BaseDriver import BaseDriver
from Base.BaseOperate import BaseOperate
from Base.BaseMethod import is_exist_element
from appium.webdriver.common.touch_action import TouchAction

# 首页-选择宠物
class ChosePet(BaseView):
    recordBtn = (By.XPATH, '//android.widget.TextView[@text="记录" and @index=1]/..')  # 发现
    petName = (By.XPATH, '//android.view.View[@index=2]/android.widget.TextView[@index=1]')    # 记录页-宠物名称
    chosePetBtn = (By.XPATH, '//android.widget.TextView[@text="选择宠物"]') # 记录页-选择宠物按钮
    petList = ["呼呼", "球球", "香猪"]    # 登录账号的宠物列表（添加的宠物数量需>=2）

    addPetBtn = (By.XPATH, '//android.widget.TextView[@text="添加"]') # 我的宠物页-添加按钮
    catBtn = (By.XPATH, '//android.widget.TextView[@text="喵星人"]') # 宠物品种页-喵星人选项

    nameBox = (By.XPATH, '//android.widget.EditText[@text="昵称最多可输入6个字"]')   # 宠物添加页-昵称输入框
    sexSelectBox = (By.XPATH, '//android.widget.TextView[@text="选择宠物性别"]')  # 宠物添加页-性别下拉框
    maleBtn = (By.XPATH, '//android.widget.TextView[@text="公"]')    # 宠物添加页-性别下拉框-公

    breedSelectBox = (By.XPATH, '//android.widget.TextView[@text="选择宠物品种"]')    # 宠物添加页-品种下拉框
    breedBtn = (By.XPATH, '//android.widget.ListView[@index=0]/android.widget.LinearLayout[@index=2]')  # 品种选择-奥西猫

    birthdaySelectBox = (By.XPATH, '//android.widget.TextView[@text="选择出生日期"]') # 宠物添加页-出身日期选择框
    monthSelectBox = (By.ID, 'com.pets.mhcw:id/dpv_month')  # 宠物添加页-出身日期选择框-月份选择
    confirmBtn = (By.ID, 'com.pets.mhcw:id/tv_confirm')   # 宠物添加页-出身日期选择框-确定按钮

    goHomeSelectBox = (By.XPATH, '//android.widget.TextView[@text="选择到家日期"]') # 宠物添加页-到家日期选择框
    weightBox = (By.XPATH, '//android.widget.EditText[@text="输入(单位kg)"]')   # 宠物添加页-体重输入框

    vaccineSelectBox = (By.XPATH, '//android.widget.TextView[@text="选择疫苗情况"]')  #宠物添加页-疫苗情况选择框
    vaBtn = (By.XPATH, '//android.widget.TextView[@text="已打全疫苗"]')  #宠物添加页-疫苗情况选择框-已打全疫苗

    sterilizationBox = (By.XPATH, '//android.widget.TextView[@text="选择绝育情况"]')  # 宠物添加页-绝育情况选择框
    steBtn = (By.XPATH, '//android.widget.TextView[@text="未绝育"]')   # 宠物添加页-绝育情况选择框-已绝育

    saveBtn = (By.XPATH, '//android.widget.TextView[@text="保存"]')   # 宠物添加页-保存按钮
    name = "996"
    weight = "2"

    newPetBtn = (By.XPATH, '//android.widget.TextView[@text={}]'.format(name))  # 我的宠物页-新增宠物
    deleteBtn = (By.XPATH, '//android.widget.TextView[@text="删除"]') # 宠物详情页-删除按钮
    conDeleteBtn = (By.XPATH, '//android.widget.TextView[@text="狠心删除"]')    # 宠物详情页-删除确认弹窗
    backBtn = (By.XPATH, '//android.widget.TextView[@text="我的宠物"]/../android.view.View[@index=1]') # 我的宠物页-返回按钮

    # 切换宠物
    def change_pet(self):
        log.info("===当前方法：%s，验证切换宠物功能===" % p.get_current_function_name())

        # 获取记录页展示的宠物名称
        petNameElement = self.driver.find_element(*self.petName)
        pet_name = petNameElement.text
        log.info("页展示当前宠物为：{}".format(pet_name))
        time.sleep(1)

        # 记录页进入我的宠物页面
        chosePetElement = self.driver.find_element(*self.chosePetBtn)
        chosePetElement.click()
        log.info("进入我的宠物页面")
        time.sleep(1)

        # 从宠物列表中随机选择宠物（所选择的宠物不同于首页当前展示的宠物）
        # self.petList.remove(pet_name)
        # new_pet = random.choice(self.petList)
        # print(new_pet)
        # petBtn = (By.XPATH, '//android.widget.TextView[@text={}]'.format(new_pet))
        if pet_name == "香猪":
            el = '//android.widget.TextView[@text="球球"]'
            # new_pet = "球球"
        else:
            el = '//android.widget.TextView[@text="香猪"]'
            # new_pet = "香猪"
        petBtn = (By.XPATH, el)
        self.driver.find_element(*petBtn).click()
        # 正则表达式获取切换的宠物名称
        new_pet = re.findall(r'@text="(.*?)"', el)
        log.info("点击宠物：{}，进行宠物切换".format(new_pet[0]))
        time.sleep(1)

    # 添加宠物
    def add_pet(self):
        log.info("===当前方法：%s，验证添加宠物功能===" % p.get_current_function_name())

        # 首页切换至记录页
        # recordElement = self.driver.find_element(*self.recordBtn)
        # recordElement.click()
        # log.info("首页跳转至发现页")
        # time.sleep(1)

        # 记录页进入我的宠物页面
        chosePetElement = self.driver.find_element(*self.chosePetBtn)
        chosePetElement.click()
        log.info("进入我的宠物页面")
        time.sleep(1)

        # 点击宠物品种页-喵星人-添加宠物页面
        addPetElement = self.driver.find_element(*self.addPetBtn)
        addPetElement.click()
        time.sleep(1)
        catElement = self.driver.find_element(*self.catBtn)
        catElement.click()
        log.info("选择喵星人，进入添加宠物页")
        time.sleep(1)

        # 填写昵称
        nameElement = self.driver.find_element(*self.nameBox)
        nameElement.send_keys(self.name)
        time.sleep(1)

        # 填写性别
        sexElement = self.driver.find_element(*self.sexSelectBox)
        # 第一次点击隐藏输入框，再次点击弹窗
        sexElement.click()
        sexElement.click()
        time.sleep(1)
        maleElement = self.driver.find_element(*self.maleBtn)
        sex = maleElement.text
        maleElement.click()
        log.info("填写昵称：{}，性别选择：{}".format(self.name, sex))
        time.sleep(1)

        # 选择品种
        breedElement = self.driver.find_element(*self.breedSelectBox)
        breedElement.click()
        time.sleep(3)
        breedBtnElement = self.driver.find_element(*self.breedBtn)
        breed = breedBtnElement.text
        breedBtnElement.click()
        log.info("品种选择：{}".format(breed))
        time.sleep(1)

        # 选择出生日期
        birthdayElement = self.driver.find_element(*self.birthdaySelectBox)
        birthdayElement.click()
        time.sleep(1)
        log.info("设置出生日期")
        # 获取月份选择元素左上角坐标
        monthElement = self.driver.find_element(*self.monthSelectBox)
        m_point = monthElement.location
        m_x = m_point['x']
        m_y = m_point['y']
        # 获取取消按钮元素左上角坐标
        confirmElement = self.driver.find_element(*self.confirmBtn)
        c_point = confirmElement.location
        c_y = c_point['y']
        # 构造需要滑动到的新的坐标点
        x = m_x
        y = m_y + (m_y - c_y)*2
        # 滑动选择月份
        TouchAction(self.driver).long_press(monthElement).move_to(x=x, y=y).release().perform()
        time.sleep(1)
        confirmElement.click()
        time.sleep(1)

        # 选择到家日期
        goHomeElement = self.driver.find_element(*self.goHomeSelectBox)
        goHomeElement.click()
        time.sleep(1)
        log.info("设置到家日期")
        # 获取月份选择元素左上角坐标
        monthElement = self.driver.find_element(*self.monthSelectBox)
        m_point = monthElement.location
        m_x = m_point['x']
        m_y = m_point['y']
        # 获取取消按钮元素左上角坐标
        confirmElement = self.driver.find_element(*self.confirmBtn)
        c_point = confirmElement.location
        c_y = c_point['y']
        # 构造需要滑动到的新的坐标点
        x = m_x
        y = m_y + (m_y - c_y)*1.5
        # 滑动选择月份
        TouchAction(self.driver).long_press(monthElement).move_to(x=x, y=y).release().perform()
        time.sleep(1)
        confirmElement.click()
        time.sleep(1)

        # 页面上滑
        BaseOperate(self.driver).swipeUp()
        time.sleep(1)

        # 填写体重
        weightElement = self.driver.find_element(*self.weightBox)
        weightElement.send_keys(self.weight)
        log.info("填写体重：{}".format(self.weight))
        time.sleep(1)

        # 疫苗情况
        vaccineElement = self.driver.find_element(*self.vaccineSelectBox)
        vaccineElement.click()
        time.sleep(0.5)
        vaccineElement.click()
        time.sleep(1)
        vaElement = self.driver.find_element(*self.vaBtn)
        va = vaElement.text
        vaElement.click()
        log.info("疫苗情况：{}".format(va))
        time.sleep(1)

        # 绝育情况
        sterilizationElement = self.driver.find_element(*self.sterilizationBox)
        sterilizationElement.click()
        time.sleep(1)
        steElement = self.driver.find_element(*self.steBtn)
        ste = steElement.text
        steElement.click()
        log.info("绝育情况：{}".format(ste))
        time.sleep(1)

        # 点击保存，跳转至记录页
        saveElement = self.driver.find_element(*self.saveBtn)
        saveElement.click()
        time.sleep(2)

        # 判断宠物是否添加成功
        boo = is_exist_element(self.driver, self.name)
        if boo == True:
            log.info("宠物添加成功！")
        else:
            log.error("宠物添加失败！")

    # 删除宠物
    def delete_pet(self):
        log.info("===当前方法：%s，验证删除宠物功能===" % p.get_current_function_name())

        # 记录页点击新增的宠物名称，进入宠物详情页
        newPetElement = self.driver.find_element(*self.newPetBtn)
        newPetElement.click()
        log.info("进入宠物详情页")
        time.sleep(1)

        # 点击删除按钮
        deleteElement = self.driver.find_element(*self.deleteBtn)
        deleteElement.click()
        log.info("点击删除按钮")
        time.sleep(1)

        # 点击确认删除按钮，页面跳转至首页
        conDeleteElement = self.driver.find_element(*self.conDeleteBtn)
        conDeleteElement.click()
        log.info("点击确认删除按钮")
        time.sleep(2)

        # 首页切换至记录页
        recordElement = self.driver.find_element(*self.recordBtn)
        recordElement.click()
        log.info("首页跳转至发现页")
        time.sleep(1)

        # 判断是否删除成功
        boo = is_exist_element(self.driver, self.name)
        if boo == True:
            log.info("宠物删除成功！")
        else:
            log.error("宠物删除失败！")

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    chosePet = ChosePet(driver)
    # chosePet.change_pet()
    chosePet.add_pet()
    # chosePet.delete_pet()