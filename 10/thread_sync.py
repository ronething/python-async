# -*- coding:utf-8 _*-

__author__ = 'ronething'

from threading import Lock, RLock
import threading

# RLock 在同一线程里面可以连续调用多次 acquire 不过要和 release 成双成对

# 加锁保持同步 会影响性能 同时可能引起死锁
lock = Lock()
# lock = RLock()
total = 0


def add():
    global lock
    global total
    for _ in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global lock
    global total
    for _ in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=desc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(total)