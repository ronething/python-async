# -*- coding:utf-8 _*-

__author__ = 'ronething'


def gen_func():
    try:
        yield 1
    except:
        pass
    yield 2
    yield 3


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen)) # 1
    print(gen.throw(Exception, 'error'))  # 2
    print(next(gen)) # 3