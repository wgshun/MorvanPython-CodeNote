# 首先需要定义一个类
class Calculator: # 通用的一个标准就是类的名字首字母一般要大写
    # __init__函数定义类的一些初始属性，功能等
    def __init__(self, weight, name='Good calculator', price=18):# 默认参数要在非默认参数的后面
        self.name = name
        self.price = price
        self.weight = weight
    def add(self, x, y): # 定义类的一个函数功能
        result = x + y # 函数体
        print(result) # 函数体

    def minus(self, x, y): # 定义类的一个函数功能
        print(x - y) # 函数体

    def times(self, x, y): # 定义类的一个函数功能
        print(x * y) # 函数体

    def divide(self, x, y): # 定义类的一个函数功能
        print(x / y) # 函数体

# 实例化calculator类,并传入__init__函数的参数
cal = Calculator(name='Bad calculator', weight=10)
print(cal.name) # 输出cal的name属性
cal.times(3,3) # 执行cal的times乘法功能