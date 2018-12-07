# Tkinter 简易窗口例子

import tkinter as tk

# 定义窗口的显示信息：标题，大小尺寸
window = tk.Tk()
window.title('first window')
window.geometry('300x200')

var = tk.StringVar()
# 创建一个在窗口显示的标签并设置相关属性：显示文本、背景颜色、字体样式和大小、显示标签的尺寸
l = tk.Label(window, textvariable=var, bg='yellow', font=('Arial', 12), width=12, height=3)
# 使用pack函数把创建的标签放到窗口上
l.pack()
# 定义一个按钮的点击状态
on_hit = False
# 定义按钮点击的函数
def hit():
    # 获取全局变量的修改权限
    global on_hit
    # 初始第一下点击
    if on_hit == False:
        on_hit = True
        var.set('you hit')
    # 初始第二下点击
    else:
        on_hit = False
        var.set('')
# 定义按钮的各项属性：显示文字、尺寸、调用函数
b = tk.Button(window, text='hit', width=9, height=1, command=hit)
# 将按钮放置在窗口中
b.pack()

# 最后使用mainloop函数来展示窗口，并实现循环更新窗口的信息
window.mainloop()