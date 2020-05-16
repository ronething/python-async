# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 对于 io 操作来说，多线程和多进程性能差别不大
# 1.通过 thread 类实例化

import time
import threading


def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url started')
    time.sleep(2)
    print('get detail url end')


# 通过继承 Thread 来实现多线程


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail html started')
        time.sleep(2)
        print('get detail html end')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(2)
        print('get detail url end')


if __name__ == "__main__":
    t1 = GetDetailHtml('get_detail_html')
    t2 = GetDetailUrl('get_detail_url')
    # t1 = threading.Thread(target=get_detail_url, args=('', ))
    # t2 = threading.Thread(target=get_detail_html, args=('', ))
    # 如果设置为 Daemon 守护进程 则 主线程执行完毕 子线程不再运行
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    start_time = time.time()
    t1.start()
    t2.start()
    # join 阻塞
    t1.join()
    t2.join()
    end_time = time.time()
    print('use time: {}'.format(end_time - start_time))
