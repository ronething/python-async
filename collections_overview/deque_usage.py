# -*- coding:utf-8 _*-

__author__ = 'ronething'

from collections import deque
"""
deque 双向队列
deque GIL 是线程安全的 list 不是线程安全的
"""

user_deque = deque(['panda', ['xzx', 'pp'], 'ronething'])

# user_deque.appendleft('zz') # deque(['zz', 'panda', ['xzx', 'pp'], 'ronething'])
# print(user_deque)

# user_deque.popleft()
# user_deque.pop()

# 浅拷贝
# str 不可变 list 可变
user_deque2 = user_deque.copy()
user_deque[0] = 'xzx'
# deque(['xzx', ['xzx', 'pp'], 'ronething']) deque(['panda', ['xzx', 'pp'], 'ronething'])
print(user_deque, user_deque2)
user_deque[1].append('lin')
# deque(['xzx', ['xzx', 'pp', 'lin'], 'ronething']) deque(['panda', ['xzx', 'pp', 'lin'], 'ronething'])
print(user_deque, user_deque2)
print(id(user_deque), id(user_deque2))

# 深拷贝
import copy
user_deque3 = copy.deepcopy(user_deque)
user_deque[1].append('Aaron')
print(user_deque, user_deque3)
print(id(user_deque), id(user_deque3))
