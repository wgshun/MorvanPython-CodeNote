# 面对对象编程时会有类的这个概念
# 简单的来说一个人就算是一个类，这个人的身高，体重，年龄等就是这个类的属性，这个人可以敲代码，可以赚钱等这就是这个人的功能

# 首先需要定义一个类
class Calculator: # 通用的一个标准就是类的名字首字母一般要大写
    name = 'Good Calculator' # 定义类的一个属性
    price = 16 # 定义类的一个属性
    def add(self, x, y): # 定义类的一个函数功能
        result = x + y # 函数体
        print(result) # 函数体

    def minus(self, x, y): # 定义类的一个函数功能
        print(x - y) # 函数体

    def times(self, x, y): # 定义类的一个函数功能
        print(x * y) # 函数体

    def divide(self, x, y): # 定义类的一个函数功能
        print(x / y) # 函数体

# 调用定义的类，首先实例化这个类
cal = Calculator()
print(cal.name) # 输出类的name属性
cal.add(1, 1) # 调用类的add函数功能
cal.minus(1, 1) # 调用类的minus函数功能