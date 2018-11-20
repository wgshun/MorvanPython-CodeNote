# 现在往刚刚写好的文件里添加一些字符

# 首先还是定义需要添加的字符
append_text = '\nThis is appended file.'

# 以append追加的方式打开my_file.txt
my_file = open('my_file.txt', 'a')
# 将追加的字符写入
my_file.write(append_text)
# 关闭my_file.txt
my_file.close()