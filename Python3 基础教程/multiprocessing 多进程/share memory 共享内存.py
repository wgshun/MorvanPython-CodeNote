# 在多线程程序中可以使用global来定义全局变量，每个线程都可以去访问改变这个变量，这个变量就是多线程所共享的
# 多线程程序说到底还是在一个核上面运行的，但多进程程序使用的是多核去运行
# 在多进程程序中使用global来定义全局变量的方法是行不通的，这时候就需要用到share memory(共享内存)了

# 例子
import multiprocessing as mp

# 使用Value函数创建共享内存的普通数据类型变量，i指int f指float（更多参考:https://docs.python.org/3.6/library/array.html）
value = mp.Value('i', 1)
# 使用Array函数创建共享内存的数组类型变量，只定义一维的数组
array = mp.Array('i', [1, 1, 1])
