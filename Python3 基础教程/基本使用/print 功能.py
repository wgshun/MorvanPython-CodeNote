# 输出函数print
# python3是print(), python2是print+空格

# 输出常数6,
print(6)

# 输出字符串
print('I am wgshun.')

# 输出带英文缩写的字符串有两种方法
print("I'm wgshun.")
print('I\'m wgshun.')

# 输出字符串组合
print('a'+'b')
# 输出字母加数字时数字也要作字符串处理，否则会报错
print('a'+'6')
print('a'+str(6))

# 输出组合时可以直接加 ，这种情况数据类型不同的也能在一个print里面输出
print('a', 'b')
print('a', 6)

# 输出常数加常数
print(6+6)
# 输出字符串形式的加法过程
print('6+6')
# 输出字符串形式的数字加常数形式的数字，先对字符串形式的数字进行常数化处理
print(int('6')+6)

# 输出小数加常数或小数
print(float(6.6)+6)
print(6.6+6.6)

