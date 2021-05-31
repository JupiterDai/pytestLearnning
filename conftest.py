#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 10:23
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture
def  ini():
    print('初始化')
    yield print('恢复')

@pytest.fixture
def  login():
    print('login正在被调用')

@pytest.fixture()
def  create():
    print('正在调用create')

@pytest.fixture(autouse=False)
def  demo():
    print('==auto==')