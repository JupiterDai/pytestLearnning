#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 7:20
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_markDemo.py
# @Software: PyCharm
#执行用例时候添加-m + markname,执行多个标记 -m 'name or name'
import pytest

@pytest.mark.weibo
def test_weibo(ini):
    print("测试微博")


@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")


@pytest.mark.toutiao
def test_toutiao1():
    print("再次测试头条")


@pytest.mark.xinlang
class TestClass:
    def test_method(self):
        print("测试新浪")


def testnoMark():
    print("没有标记测试")