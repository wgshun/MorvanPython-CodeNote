# 在python的多线程中线程之间是不能直接返回值
# queue功能用来接收多线程运算的结果，实现线程间安全的数据交互

import threading
from queue import Queue
# Queue 是一个队列，存取数据是先进先出
# 定义一个任务函数
def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    # Queue 的put功能是往队列里存数据
    q.put(l)

def multithreading():
    # 定义一个队列Queue
    q = Queue()
    # 定义一个列表用来存放多个线程
    threads = []
    # 定义需要多线程运算的初始数据
    data = [[2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5 ,5]]
    # for循环创建四个线程分别执行一个任务函数
    for i in range(4):
        # 定义一个线程执行job函数，传进去两个参数（需要运算的数据，存放运算结果的队列）
        t = threading.Thread(target=job, args=(data[i], q))
        # 启动线程
        t.start()
        # 将创建的线程加入到列表
        threads.append(t)
    # 循环多线程列表，分别执行join函数
    for thread in threads:
        thread.join()
    # 定义一个列表接收队列里面的运算结果
    results = []
    # 循环使用get()函数取出队列中的运算结果
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__ == '__main__':
    multithreading()