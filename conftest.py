#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 10:23
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope='session')
def  ini():
    print('初始化')