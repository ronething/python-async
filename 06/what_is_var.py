# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
python 变量和 java 的本质不一样
python 变量实质是一个指针
"""

a = [1, 2, 3]
b = a
b.append(4)
print(a, id(a), id(b))  # [1, 2, 3, 4] 4486942536 4486942536

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(id(a), id(b), a is b, a == b)  # 4538762632 4537984712 False True
