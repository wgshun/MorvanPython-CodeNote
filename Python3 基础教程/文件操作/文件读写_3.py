# 读取文件的主要方式

# 以read的方式打开文件
file = open('my_file.txt', 'r') # 读取到的是一个文件形式

# content = file.read() # 读取文件中的所有内容
# print(content)

# content_first = file.readline() # 逐行读取文件中的内容,且第一次执行读取文件的第一行内容
# print(content_first)
# content_second  = file.readline() # 逐行读取文件中的内容，第二次执行读取文件的第一行和第二行内容
# print(content_second)

content_all = file.readlines() # 逐行读取文件中的所有内容，读取出来的内容放到一个list列表中
print(content_all)