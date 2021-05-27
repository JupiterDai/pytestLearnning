#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:25
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_compare.py.py
# @Software: PyCharm
import pytest


def test_greater(ini):
    num = 100
    assert num > 100


def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.less
def test_less():
    num = 100
    assert num < 200
