# 多进程的进程锁 Lock ，多进程的进程锁作用同多线程的线程锁

# 例子

import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()

# 以上例子加上lock相关操作之前进程一和进程二会共享同一内存导致两个进程的结果交叉输出，且互相影响
# 加上lock相关操作之后两个进程就相对独立了，进程二会等进程一执行结束了以后再执行，不会互相影响