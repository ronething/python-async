# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
列表(生成式)推导式
不可滥用 可读性
"""

odd_list = [i for i in range(20) if i % 2 == 1]
print(odd_list)
"""
生成器表达式
"""

odd_gen = (i for i in range(20) if i % 2 == 1)
print(type(odd_gen))  # <class 'generator'>
"""
字典推导式
"""

my_dict = dict(user='ronething', age=18)
reversed_dict = {v: k for k, v in my_dict.items()}
print(reversed_dict)
"""
集合推导式
"""

my_set = {k for k, v in my_dict.items()}
print(my_set)
