# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
tuple 比 list 好的地方
- immutable
    - 性能优化
    - 线程安全
    - 可以作为 dict 的 key
    - 拆包特性
如果拿 C lang 类比，tuple 对应 struce 、list 对应 array
"""

from collections import namedtuple

# 使用 namedtuple 创建一个类

User = namedtuple('User', ['name', 'age', 'height'])
user_tuple = ('ronething', 20, 126)
user = User(*user_tuple)
user_info = user._asdict()  # OrderedDict([('name', 'ronething'), ('age', 20), ('height', 126)])
# user = User._make(user_tuple) 与上面一样效果
print(user.name, user.age, user.height)
