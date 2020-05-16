# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 进程之间数据独立隔离

from multiprocessing import Pool, Queue, Process, Manager, Pipe
import time


def producer(queue):
    queue.put('a')
    time.sleep(2)


def customer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


def pipe_prod(pipe):
    pipe.send('panda')


def pipe_cust(pipe):
    print(pipe.recv())


def add_key(p, k, v):
    p[k] = v


if __name__ == "__main__":
    # from queue import Queue 无法用于进程之间的通信
    # ⚠️ 普通的进程间通信可以使用 multiprocessing 中的 Queue
    # queue = Queue(10)
    # p1 = Process(target=producer, args=(queue, ))
    # p2 = Process(target=customer, args=(queue, ))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # ⚠️multiprocessing 中的 Queue 无法用于 pool 创建的进程池进程间的通信
    # 需要使用 manager 中的 queue
    # queue = Manager().Queue(10)
    # pool = Pool(2)
    # pool.apply_async(producer, args=(queue, ))
    # pool.apply_async(customer, args=(queue, ))

    # pool.close()
    # pool.join()

    # pipe 性能高于 queue 只能用于两个进程间通信
    # receive_pipe, send_pipe = Pipe()  # receive_pipe, send_pipe 命名而已 无所谓顺序
    # p1 = Process(target=pipe_prod, args=(send_pipe, ))
    # p2 = Process(target=pipe_cust, args=(receive_pipe, ))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # 内存共享 Manager
    # 使用普通的 dict 是无法共享的 Manager 类中还有其他类型可供使用
    # 使用共享需要考虑同步问题 跟线程中的差不多 condition semaphore
    p_dict = Manager().dict()
    p1 = Process(target=add_key, args=(p_dict, 'user1', 'panda'))
    p2 = Process(target=add_key, args=(p_dict, 'user2', 'ronething'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(p_dict)  # {'user1': 'panda', 'user2': 'ronething'}
