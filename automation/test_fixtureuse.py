#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 6:08
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_fixtureuse.py
# @Software: PyCharm


import pytest
def test_login2(login):
    flag = 1
    print('调用login')
    assert flag==1

@pytest.mark.usefixtures('ini','create')
def test_login3():
     flag = 1
     print('正在测试login3')
     assert flag==1

def test_loginDemo():
    flag = 1
    print('正在测试demo')
    assert flag == 1
