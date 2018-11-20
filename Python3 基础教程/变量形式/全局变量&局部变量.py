# 全局变量的定义通常会全部大写，定义的全局变量可以在此脚本下随意调用
A = 1
def fun():
    # bp在此就是局部变量，这个变量只能在函数fun()下使用
    bp = 10
    # 在函数里也可以改变一个全局变量，要使用到global,如果不使用global，改变的只是在fun函数里生效，不是全局性的
    global A
    A = 10
    return bp + A

print(A) # 输出改变前的全局变量a
print(fun())
print(A) # 输出改变后的全局变量a