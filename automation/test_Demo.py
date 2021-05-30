#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 7:07
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_Demo.py
# @Software: PyCharm
#跳过测试用例@pytest.mark.skip
import  pytest

@pytest.fixture(autouse=True)
def   clear():
    print('=======auto clear =======')

def test_case1():
    print('测试用例1')

@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")