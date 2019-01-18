# 可拉动的一个‘尺度条’，将拉动的尺度反馈到文本框

import tkinter as tk

window = tk.Tk()
window.title('MY')
window.geometry('200x200')

l = tk.Label(window, bg='green', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text=v)

# orient参数表示尺度条是横向还是纵向
# showvalue参数表示拉动的进度条数字是否显示
# tickinterval参数表示进度条分为几部分
# resolution参数表示进度条显示数值的最小单位
s = tk.Scale(window, label='try it', from_=5, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,
             tickinterval=3, resolution=0.1, command=print_selection)
s.pack()

window.mainloop()