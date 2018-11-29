# 读取一个文件的时候，文件不存在，就会报错
# 加上try...except...之后就可以捕获这个错误，并且自定义显示这个错误的方式，根据需要对这个错误做处理

try:
    file = open('test', 'r')
except Exception as e: # 将这个错误赋值给变量e
    print('There is no file named test.') # 输出其定义的错误信息
    re = input('Do you want to create a new file? y/n') # 交给用户做决定需不需要创建一个新文件
    if re == 'y': # 判断是否创建新文件，是
        file = open('test', 'w') # 创建新文件
    else: # 否
        pass # 跳过
else:# 接上面的try，如果没错误往下执行
    file.close()