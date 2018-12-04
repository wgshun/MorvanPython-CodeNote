# Pool 进程池：把需要运行的计算放到进程池里，python就会自己调配进程和线程去运算最后返回运算结果

# 下面看例子

import multiprocessing as mp

def job(x):
    return x * x

def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10000))
    print(res)

if __name__ == '__main__':
    multicore()