# input 函数可以在程序运行时提供输入的功能

input_1 = input('Please give a number:')

print('This input number is:', input_1)
# input 函数的返回值是一个字符串形式
if input_1 == '6':
    print('You are a good boy.')
else:
    print('See you.')