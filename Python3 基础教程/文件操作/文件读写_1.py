# 首先定义一个字符串
text = "This is my first text.\nThis is next line.\nThis is last line."
# 以write的方式打开一个txt文件
my_file = open('my_file.txt', 'w')
# 将刚刚定义的字符串写入到打开的txt文件中
my_file.write(text)
# 关闭打开的txt文件
my_file.close()