# 一般多线程工作的时候会启动一个主线程和多个子线程
# 当主线程的任务比子线程的任务少时，主线程要比子线程先结束
# join的功能是当主线程任务做完之后，进入阻塞状态，等到调用join功能的子线程工作结束了，主线程再结束
# 当有多个线程时，根据需要调用join函数
# 详情如下例子：

import threading
import time

# 创建线程1的工作函数
def t1_job():
    print('t1 start.\n')
    # 定义循环工作，time.sleep(0.1)进入休眠状态0.1秒
    for i in range(10):
        time.sleep(0.1)
    print('t1 end.\n')

def main():
    # 创建线程1并指定工作，名称
    thread1 = threading.Thread(target=t1_job, name='t1')
    # 线程1开始运行
    thread1.start()
    # 不加join时，控制台会依次输出：t1 start -> all done -> t1 end,即主线程比t1线程先结束
    # 加join时，控制台会依次输出：t1 start -> t1 end -> all done,即当主线程任务做完之后，会等待t1线程先结束
    # thread1.join()
    print('all done.\n')


if __name__ == '__main__':
    main()