# -*- coding:utf-8 _*-

__author__ = 'ronething'

from collections import Counter
"""
Counter dict 的子类
可以传入任意可迭代对象
"""

users = ['panda', 'xzx', 'ronething', 'panda']
users_counter = Counter(users)
str_counter = Counter('qweqwqweeasdxcvzxcv')
print(users_counter)  # Counter({'panda': 2, 'xzx': 1, 'ronething': 1})
print(str_counter)  # Counter({'q': 3, 'w': 3, 'e': 3, 'x': 2, 'c': 2, 'v': 2, 'a': 1, 's': 1, 'd': 1, 'z': 1})
str_counter.update('qwe')
str_counter.update(users_counter)
# top n 问题 本质是 堆排序
print(str_counter.most_common(2))
print(str_counter)