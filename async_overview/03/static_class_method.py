# -*- coding:utf-8 _*-

__author__ = 'ronething'


class Date:
    def __init__(self, year, month, day):
        """构造方法"""
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        """实例方法"""
        self.day += 1

    @staticmethod
    def parse_from_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        # 此时 Date 硬编码如果 class Date 修改则这里也需要修改
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        """静态方法的好处 如果不需要 self 也不需要 cls 可以使用这种"""
        pass

    @classmethod
    def from_str(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        # cls 类对象 类是对象 type 的实例 请看前面 type class object 的关系
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(
            year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2019, 3, 20)
    new_day.tomorrow()
    print(new_day)
    date_str = '2019-03-20'

    # staticmethod
    other_day = Date.parse_from_str(date_str)
    print(other_day)

    # class method
    another_day = Date.from_str(date_str)
    print(another_day)
