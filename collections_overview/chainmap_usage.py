# -*- coding:utf-8 _*-

__author__ = 'ronething'

from collections import ChainMap
"""
ChainMap


"""

user_dict1 = {'a': 'panda', 'b': 'ronething'}
user_dict2 = {'c': 'xzx', 'd': 'pp'}
"""
以往要遍历多个字典是这样的
"""
for k, v in user_dict1.items():
    pass

for k, v in user_dict2.items():
    pass
"""
使用 ChainMap
如果字典中有重复的项只会输出一个
"""
new_dict = ChainMap(user_dict1, user_dict2)
for k, v in new_dict.items():
    print(k, v)
# new_child New ChainMap with a new map followed by all previous maps.
other_dict = new_dict.new_child({'e': 'zz'})
print(other_dict.maps)
for k, v in new_dict.items():
    print(k, v)
