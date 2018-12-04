# 节选自：https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/1-why/
# multiprocessing 和 threading 的比较
# 多进程 Multiprocessing 和多线程 threading 类似, 他们都是在 python 中用来并行运算的.
# 不过既然有了 threading, 为什么 Python 还要出一个 multiprocessing 呢?
# 原因很简单, 就是用来弥补 threading 的一些劣势, 比如在 threading 中提到的GIL.
#   （实际上，python解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。
#       GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势。）
# 目前的计算机都会有多核的处理器，我们可以调用python的multiprocessing库来使用多核多进程来运行python程序，充分发挥多核处理器的作用
