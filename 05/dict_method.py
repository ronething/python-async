# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
dict 使用 C 语言实现
"""

a = {
    'user1': 'panda',
    'user2': 'ronething',
}

# 清除所有元素
a.clear()

# copy 浅拷贝
new_dict = a.copy()

# fromkeys
new_list = ['xzx', 'pp']
fromkeys_dict = dict.fromkeys(new_list, 'user')
print(fromkeys_dict)  # {'xzx': 'user', 'pp': 'user'}

v = new_dict.setdefault('user3', 'xzx')  # xzx
print(new_dict)  # {'user3': 'xzx'}

another_dict = {'user4': 'pp'}
new_dict.update(another_dict)
print(new_dict)  # {'user3': 'xzx', 'user4': 'pp'}
