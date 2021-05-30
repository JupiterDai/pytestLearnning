#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 6:08
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_fixtureuse.py
# @Software: PyCharm
import pytest


def test_login(login):
    print('调用login')