# 自定义的一个输出当前时间的函数方法

# 载入time模块的localtime函数
from time import localtime
# 一个方法可以返回localtime函数返回的当前时间
def printtime():
    return localtime()