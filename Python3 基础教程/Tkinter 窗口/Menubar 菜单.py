# tkinter 菜单栏

import tkinter as tk

window = tk.Tk()
window.title('window menubar')
window.geometry('600x600')

l = tk.Label(window, bg='yellow', width=60)
l.pack()

counter = 0
def do_job():
    global counter
    counter += 1
    # 改变
    l.config(text='do'+str(counter))

# 创建菜单栏，显示在窗口的上方
menubar = tk.Menu(window)
# 创建菜单栏里的菜单集合单元
filemenu = tk.Menu(menubar, tearoff=0)# tearoff设置为1的话，创建的菜单栏可以独立于窗口存在, 默认为1
menubar.add_cascade(label='file', menu=filemenu)# 给创建的菜单命名
# 创建菜单单元的菜单操作
filemenu.add_command(label='new', command=do_job)# 点击菜单会执行do_job函数
filemenu.add_command(label='open', command=do_job)
# 菜单单元的菜单分割线
filemenu.add_separator()
# 创建一个退出窗口的菜单选项
filemenu.add_command(label='exit', command=window.quit)

filemenu.add_separator()
# 在创建的菜单集合单元里再创建一个菜单集合单元然后创建菜单列表及下属菜单
submenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='submite', menu=submenu, underline=0)
submenu.add_command(label='sub1', command=do_job)

# 将创建的菜单栏设置到window窗口
window.config(menu=menubar)

# 展示窗口
window.mainloop()