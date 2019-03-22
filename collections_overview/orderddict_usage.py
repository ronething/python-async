# -*- coding:utf-8 _*-

__author__ = 'ronething'

from collections import OrderedDict

user_order_dict = OrderedDict()

user_order_dict['b'] = 'panda'
user_order_dict['a'] = 'ronething'
user_order_dict['c'] = 'xzx'

print(user_order_dict.move_to_end('b'))
print(user_order_dict)
print(user_order_dict.popitem())
print(user_order_dict)