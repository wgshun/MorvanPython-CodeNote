# Tkinter 简易窗口例子
# 列表部件，选择列表中的元素，点击按钮，使之显示在窗口标签中

import tkinter as tk

# 定义窗口的显示信息：标题，大小尺寸
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
# 定义显示信息的标签
l = tk.Label(window, bg='green', width=3, textvariable=var1)
l.pack()

# 将选中的列表元素赋值给
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', command=print_selection)
b1.pack()
var2 = tk.StringVar()
var2.set((1, 2, 3, 4, 5, 6))
lb = tk.Listbox(window, listvariable=var2)
list_items = [11, 22, 33]
for list_item in list_items:
    lb.insert('end', list_item)
lb.insert(1, 'one')
lb.insert(2, 'two')
lb.delete(2)
lb.pack()

# 最后使用mainloop函数来展示窗口，并实现循环更新窗口的信息
window.mainloop()
