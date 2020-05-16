# -*- coding:utf-8 _*-

__author__ = 'ronething'


def gen_func():
    html = yield 'panda'
    print(html)
    return 'panda'


if __name__ == "__main__":
    gen = gen_func()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    url = next(gen)
    # print(url)
    # next(gen)
    gen.send('xzx')
    # print(gen.send('xixixi'))