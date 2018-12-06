# Pool 进程池：把需要运行的计算放到进程池里，python就会自己调配进程和线程去运算最后返回运算结果

# 下面看例子

import multiprocessing as mp

def job(x):
    return x * x

def multicore():
    # 定义一个pool,默认使用计算机所有的核，可以使用processes参数来配置想要使用的内核数量
    pool = mp.Pool(processes=2)
    # 使用map将需要计算的函数和多个参数传入pool
    res = pool.map(job, range(10))
    print(res)
    # 使用apply_async函数，pool会只用一个核来计算，传入的参数只能是一个值，加上都好表示可迭代
    res1 = pool.apply_async(job, (2,))
    print(res1.get())
    # 使用迭代器来实现像map一样多个参数的计算,输出结果的时候也是使用迭代器获取
    multi_res1 = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res1.get() for res1 in multi_res1])


if __name__ == '__main__':
    multicore()

