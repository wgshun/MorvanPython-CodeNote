# Queue队列用于存储多进程的返回值同多进程
# Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果， 继续加载运算。
# 原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果.
# 摘选自：https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/3-queue/

import multiprocessing as mp

def job(q):
    r = 0
    for i in range(1000):
        r += i + i*2 + i*3
    q.put(r)

# 相关操作皆类似于threading
if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,)) # 传入args操作时只有一个参数时，后面需要加逗号，表示args是可迭代的
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q.get(), q.get())
