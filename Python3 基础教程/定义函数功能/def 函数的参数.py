# 定义一个函数需要用到 def 函数
def fun(a, b): # function是函数名，a和b是函数的参数
    print('This is a function.') # 函数的主体
    c = a + b # 函数的主体
    print('c is ', c)

# 为了使用刚刚定义的函数，下面需要调用它
fun(1, 2) # 1和2就是传进去的参数，参数的默认顺序和定义函数时一样，不传参数python会报错
fun(a=1, b=2)# 当然也可以自定义参数的值