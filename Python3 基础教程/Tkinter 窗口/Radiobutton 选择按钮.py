# 单选按钮,选中以后将对应信息反馈到文本框

import tkinter as tk

window = tk.Tk()
window.title('My Window !')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='green', width=20)
l.pack()

def print_selection():
    l.config(text='You have selected ' + var.get())

# 定义单选按钮，选中操作会把 value 赋值给 var
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()