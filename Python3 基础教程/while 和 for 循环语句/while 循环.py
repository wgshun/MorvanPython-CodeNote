# while 循环，简单理解为当什么什么时候做什么什么事情，
#             就是满足某个条件的时候做某个事情。

condition = 1 # 定义自变量
while condition < 10: # 当自变量condition小于10的时候进入while循环执行
    print(condition) # 输出当前自变量的值
    condition += 1 # 使自变量在原来的基础上加1
# 上述循环输出为1-9的常数，当condition递加等于10的时候不满足循环条件跳出循环

while True:
    print("I'm True.")
# 上述循环会一直输出‘I'm True.’, 因为while循环的条件是True，只能手动停止它