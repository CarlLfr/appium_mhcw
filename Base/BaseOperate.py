#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/08/29
# @Author  : Liufeiru

import os
import time
from appium.webdriver.common.touch_action import TouchAction

class BaseOperate():
    def __init__(self, driver):
        self.driver = driver

    # 获取屏幕宽高
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipeLeft(self):
        gs = self.get_size()
        x1 = int(gs[0]*0.9)
        y1 = int(gs[1]*0.5)
        x2 = int(gs[0]*0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向右滑动
    def swipeRight(self):
        gs = self.get_size()
        x1 = int(gs[0]*0.1)
        y1 = int(gs[1]*0.5)
        x2 = int(gs[0]*0.9)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向上滑动
    def swipeUp(self):
        gs = self.get_size()
        x1 = int(gs[0]*0.5)
        y1 = int(gs[1]*0.9)
        y2 = int(gs[1]*0.1)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 向下滑动
    def swipeDown(self):
        gs = self.get_size()
        x1 = int(gs[0] * 0.5)
        y1 = int(gs[1] * 0.1)
        y2 = int(gs[1] * 0.9)
        self.driver.swipe(x1, y1, x1, y2, 1000)

# 指定元素向左滑动
def swipe_element_left(driver, element):
    # 当前元素左上角的坐标
    point = element.location
    print(point)
    # 计算移动后的位置坐标
    w = driver.get_window_size()['width']
    point_x = point['x'] - w*0.5
    point_y = point['y']
    # 滑动
    TouchAction(driver).long_press(element).move_to(x=point_x, y=point_y).release().perform()

# 根据坐标点 点击页面
def page_click(x, y):
    click_command = "adb shell input tap " + str(x) + " " +str(y)
    os.system(click_command)

if __name__ == '__main__':
    print(page_click(200, 402))