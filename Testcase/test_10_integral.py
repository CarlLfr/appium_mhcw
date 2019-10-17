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

# 验证积分功能是否正常
class IntegralSignIn(BaseView):
    myBtn = (By.XPATH, '//android.widget.TextView[@text="我的"]') # 底部tab-我的
    integralBtn = (By.XPATH, '//android.widget.TextView[@text="积分"]')  # 我的页面-积分
    myIntegral = (By.XPATH, '//android.widget.TextView[@index=4]/../../android.view.View[@index=0]/android.widget.TextView[@index=2]')  # 我的积分页-我的积分
    sevenDayBtn = (By.XPATH, '//android.view.View[@index=14]')  # 我的积分页-第七天20积分区域
    backBtn = (By.XPATH, '//android.widget.TextView[@text="我的积分"]/../android.view.View[@index=1]')  # 我的积分页-返回按钮

    # 签到
    def integral_sign_in(self):
        log.info("===当前方法：%s，验证积分签到功能是否正常===" % p.get_current_function_name())

        # 首页跳转至我的页面
        myBtnElement = self.driver.find_element(*self.myBtn)
        myBtnElement.click()
        log.info("进入我的页面")
        time.sleep(1)

        # 点击 我的-积分
        integralElement = self.driver.find_element(*self.integralBtn)
        integralElement.click()
        log.info("进入积分页面")
        time.sleep(1)

        # 获取该账号未签到之前的总积分
        myIntegralEle = self.driver.find_element(*self.myIntegral)
        before_re = myIntegralEle.text
        pre_integral = before_re.split(' ')[1]
        log.info("签到前总积分为：{}".format(pre_integral))

        # 点击第七天20积分区域
        sevenDayEle = self.driver.find_element(*self.sevenDayBtn)
        sevenDayEle.click()
        log.info("点击第七天20积分区域，签到")
        time.sleep(2)

        # 获取该账号签到之后的总积分
        myIntegralEle = self.driver.find_element(*self.myIntegral)
        after_re = myIntegralEle.text
        later_integral = after_re.split(' ')[1]
        log.info("签到前总积分为：{}".format(later_integral))

        # 通过判断签到后积分是否大于签到前积分来判断签到是否成功
        if later_integral > pre_integral:
            log.info("签到成功！")
        else:
            log.error("签到失败！")

        # 返回我的页面
        backElement = self.driver.find_element(*self.backBtn)
        backElement.click()
        time.sleep(1)

if __name__ == '__main__':
    driver = BaseDriver().Android_driver()
    time.sleep(5)
    integral = IntegralSignIn(driver)
    integral.integral_sign_in()