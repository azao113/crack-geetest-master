#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
from geetest import BaseGeetestCrack
from selenium import webdriver


class IndustryAndCommerceGeetestCrack(BaseGeetestCrack):
    """工商滑动验证码破解类"""

    def __init__(self, driver):
        super(IndustryAndCommerceGeetestCrack, self).__init__(driver)

    def crack(self):
        """执行破解程序
        """
        self.input_by_id()
        self.click_by_id()
        # time.sleep(3.5)
        x_offset = self.calculate_slider_offset()
        print x_offset
        track_list = get_track(x_offset)
        for track in track_list:
            self.drag_to_index(track)
        self.release_mouse()
            # self.drag_and_drop(x_offset=track)
#

# 根据缺口的位置模拟x轴移动的轨迹
def get_track(length):
    pass
    list = []
    list.append(1)
    length = length - 1
    # 间隔通过随机范围函数来获得,每次移动一步或者两步
    x = random.randint(1, 3)
    # 生成轨迹并保存到list内
    while length - x >= 1:
        list.append(x)
        length = length - x
        x = random.randint(1, 3)
    # 最后五步都是一步步移动
    for i in range(length):
        list.append(1)
    return list


def main():
    driver = webdriver.Chrome()
    # driver.get("http://bj.gsxt.gov.cn/sydq/loginSydqAction!sydq.dhtml")
    driver.get("http://www.gsxt.gov.cn/index.html")
    cracker = IndustryAndCommerceGeetestCrack(driver)
    cracker.crack()
    # print(driver.get_window_size())
    time.sleep(10)
    # driver.save_screenshot("screen.png")
    driver.close()


if __name__ == "__main__":
    while 1:
        main()
