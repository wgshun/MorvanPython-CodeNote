# 使用多线程首先要导入threading模块
import threading

# 定义一个函数帮助了解threading模块的基础功能
def main():
    # active_count函数的功能是计算已激活线程的数量
    print(threading.active_count())
    # enumerate函数的功能是输出已激活线程的信息
    print(threading.enumerate())
    # current_thread函数的功能是当前脚本运行的线程信息
    print(threading.current_thread())
    # 创建一个新的线程
    added_thread = threading.Thread(target=thread_job)
    # 启动创建的新线程
    added_thread.start()

def thread_job():
    print('\nThis is an added Thread.', threading.current_thread())

# 使用__name__判断直接进入主函数执行
if __name__ == '__main__':
    main()