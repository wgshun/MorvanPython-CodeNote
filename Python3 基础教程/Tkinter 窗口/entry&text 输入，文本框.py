# Tkinter 简易窗口例子
# 关于输入框，文本框，输入信息添加到文本框的两种方式

import tkinter as tk

# 定义窗口的显示信息：标题，大小尺寸
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 定义一个输入框
e = tk.Entry(window, show=None) # show='*'将你输入的东西全部显示为*
# 将输入框放置在窗口中
e.pack()

def insert_point():
    var = e.get() # 获取输入框输入的信息
    t.insert('insert', var)
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(1.3, var) # 第一个参数可以指定添加到文本的具体位置，1.1就是第一行第一列

b1 = tk.Button(window, text='insert point', command=insert_point)# 将输入的信息添加到文本框鼠标所点的位置
b2 = tk.Button(window, text='insert end', command=insert_end)# 将输入的信息添加到文本框文本的末尾

b1.pack()
b2.pack()
# 定义文本框
t = tk.Text(window, height=2) # height为文本框的行数
t.pack()

# 最后使用mainloop函数来展示窗口，并实现循环更新窗口的信息
window.mainloop()
