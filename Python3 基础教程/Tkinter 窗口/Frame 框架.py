# 窗口里的框架分布

import tkinter as tk

window = tk.Tk()
window.title('window')
window.geometry('400x200')
tk.Label(window, text='main window').pack()

# 在window窗口上创建一个框架frame
fm = tk.Frame(window)

# 在刚创建的框架里再创建两个框架
fm_l = tk.Frame(fm, bg='red')
fm_r = tk.Frame(fm, bg='green')

fm_l.pack(side='left')
fm_r.pack(side='right')

# 创建三个文本框来标识三个框架
tk.Label(fm, text='main frame').pack()
tk.Label(fm_l, text='left frame').pack()
tk.Label(fm_r, text='right frame').pack()

fm.pack()

window.mainloop()