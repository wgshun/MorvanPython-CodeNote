# 摘自https://morvanzhou.github.io/tutorials/python-basic/threading/5-GIL/
# python 的多线程 threading 有时候并不是特别理想. 最主要的原因是就是：
# Python 的设计上, 有一个必要的环节, 就是 Global Interpreter Lock (GIL). 这个东西让 Python 还是一次性只能处理一个东西.
#
# 尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。
# 实际上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。
# GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势。（比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。
# 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。
# 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。
# 实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。

# 测试GIL例子
import threading
from queue import Queue
import copy
import time

# 定义一个使用多线程的运算求和任务
def job(l, q):
    res = sum(l)
    q.put(res)
# 定义一个多线程主函数，创建多线程执行运算任务，存取运算结果
def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)
# 定义一个非多线程的运算求和函数
def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    # 定义一个需要运算的大规模的常数列表
    l = list(range(1000000))
    s_t = time.time()
    # 调用非多线程求和运算函数
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    # 调用多线程求和运算
    multithreading(l)
    print('multithreading: ', time.time()-s_t)

# 看最终的输出结果会发现多线程的并不会比非多线程的运算快上多少甚至于更慢
# 按照我们预想的来创建了四个线程去执行求和运算，应该要比非多线程的快上3-4倍，但是并没有
# 这就是python的GIL设计