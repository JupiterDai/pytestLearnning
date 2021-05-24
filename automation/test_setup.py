#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 10:10
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_setup.py
# @Software: PyCharm
import pytest

@pytest.fixture()
def prints():
    print('gg')
