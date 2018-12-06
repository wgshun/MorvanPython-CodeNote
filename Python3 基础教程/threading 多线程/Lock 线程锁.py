# 线程锁可以暂时锁住当前线程同其他线程的共享内存不让其他线程进行访问，加上线程锁以后会让多线程间有顺序的去执行

# 线程锁例子
import threading

def job1():
    global A, lock
    lock.acquire() # 锁住
    for i in range(10):
        A += 1
        print('job1:', A)
    lock.release() # 释放

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2:', A)
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 以上例子加上lock相关操作之前线程一和线程二会共享同一内存导致两个线程的结果交叉输出，且互相影响
# 加上lock相关操作之后两个线程就相对独立了，线程二会等线程一执行结束了以后再执行，不会互相影响