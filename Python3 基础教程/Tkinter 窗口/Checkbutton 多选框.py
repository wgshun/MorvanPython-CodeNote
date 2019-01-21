# 多选框及其反馈

import tkinter as tk

window = tk.Tk()
window.title('MY')
window.geometry('300x300')

l = tk.Label(window, bg='green', width=30, text='None')
l.pack()

def print_selection():
    # 通过多个 if 判断多选框的选中状态，来控制输出的文本
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python.')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++.')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text="I don't love either.")
    else:
        l.config(text='I love both.')

var1 = tk.IntVar()
var2 = tk.IntVar()
# text为多选框显示文本，variable为多选框选中状态的赋值，onvalue为选中时的标记值，offvalue为非选中时的标记值
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()