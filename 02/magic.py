# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 魔法函数一览
# __add__ __abs__

# 字符串表示


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ",".join(self.employee)

    # 开发者用到
    def __repr__(self):
        return ",".join(self.employee)


company = Company(['Panda', 'Ronething'])

print(company)  # 会隐含调用 str(company)