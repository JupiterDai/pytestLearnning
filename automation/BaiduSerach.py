#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:08
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : BaiduSerach.py
# @Software: PyCharm
from selenium import webdriver
import time
class BaiduSerach(object):
    driver = webdriver.Edge();

    def open_baidu(self):
        self.driver.get(r'https://www.baidu.com/')
        time.sleep(1)
    def test_serach(self):
        self.driver.find_element_by_id('kw').send_keys('dota2')
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'dota2' in self.driver.title
            print('TestPASS');
        except  Exception as e:
            print('Test Fail')

baidu = BaiduSerach();
baidu.open_baidu()
baidu.test_serach()

