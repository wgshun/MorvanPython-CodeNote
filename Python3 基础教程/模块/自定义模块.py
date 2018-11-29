# 在这里调用自定义的输出当前时间的函数

# 载入自定义的模块 demo1
# Windows下使用PyCharm载入找不到自定义的模块时，可以设置demo1所在文件夹为 Sources Root
import demo1
# 调用自定义模块下输出当前时间的函数
t = demo1.printtime()
print(t)
