# Tkinter 简易窗口例子

import tkinter as tk

# 定义窗口的显示信息：标题，大小尺寸
window = tk.Tk()
window.title('first window')
window.geometry('300x200')

# 定义一个输入框
e = tk.Entry(window, show=None)
# 定义按钮的各项属性：显示文字、尺寸、调用函数
b = tk.Button(window, text='hit', width=9, height=1, command=hit)
# 将按钮放置在窗口中
b.pack()

# 最后使用mainloop函数来展示窗口，并实现循环更新窗口的信息
window.mainloop()