#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 13:03
# @Author  : Denny
# @Email   : 1305037577@qq.com
# @File    : yunsuan.py
# @Software: PyCharm
b1 = 11 > 2 # true
b2 = 11 >= 11 # true
b3 = 11 != 2 # true

a, b = 11, 12
b4 = a >= b# false

print (b1, b2, b3, b4)


a = 11 > 2
b = 1 > 9

# and and or
X = a and b
Y = a or b
Z = not a

print (a, b, X, Y, Z)

# A meaningful variable naming is important

isStudent = True
isKid = False
print (isStudent and isKid)
print (isStudent or isKid)