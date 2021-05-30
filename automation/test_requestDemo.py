#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 7:30
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : test_requestDemo.py
# @Software: PyCharm
#
import  pytest
@pytest.fixture()
def logins(request):
    param = request.param
    print(f"账号是：{param['username']}，密码是：{param['pwd']}")
    return param


data = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
]


@pytest.mark.parametrize("logins", data, indirect=True)
def test_name_pwd(logins):
    print(f"账号是：{logins['username']}，密码是：{logins['pwd']}")