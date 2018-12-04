# python 中 multiprocessing 和 threading 的使用方法几乎差不多，方便上手
# 下面是例子
# 首先还是导入相关的模块
import multiprocessing as mp

def job(x, y):
    print('t1t1t1', x, y)

# 多进程需要在__main__下去执行，直接在脚本中调用会报错
if __name__ == '__main__':
    # 由此看process和thread的使用方式是一样的
    p1 = mp.Process(target=job, args=(2, 2))
    p1.start()
    p1.join()
