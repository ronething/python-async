# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
defaultdict
"""

from collections import defaultdict

user_dict = {}
users = ['panda', 'xzx', 'ronething', 'panda']
for user in users:
    """
    以往应该是
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1
    """
    # 相当于 if user not in user_dict: user_dict[user] = 0
    user_dict.setdefault(user, 0)
    user_dict[user] += 1

print(user_dict)

# 以下使用 defaultdict

default_dict = defaultdict(int)

for user in users:
    default_dict[user] += 1

print(default_dict) # defaultdict(<class 'int'>, {'panda': 2, 'xzx': 1, 'ronething': 1})
for k, v in default_dict.items():
    print(k, v)


def gen_default():
    return {
        "name": "",
        "nums": 0,
    }


custom_default_dict = defaultdict(gen_default)
print(custom_default_dict["custom"]) # {'name': '', 'nums': 0}
