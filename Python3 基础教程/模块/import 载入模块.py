# 载入一个模块 time，才能使用该模块下的函数功能
import time
# 使用time模块中的localtime函数输出当前的时间
print(time.localtime())

# 在载入模块的时候可以使用 as 来给该模块取一个简称
import time as t
print(t.localtime())

# 如果只是想要用一个模块下的某些函数功能，就可以在载入的时候只载入模块下的该函数功能
# from 模块名 import 函数名
from time import localtime
print(localtime())

# 如果只是想要用一个模块下的所有函数功能，也可以这么载入
from time import *
print(localtime()) # time模块下的localtime函数
print(time()) # time模块下的time函数