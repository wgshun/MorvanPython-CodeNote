# window 中创建的各种小部件的放置方法

import tkinter as tk

window = tk.Tk()
window.title('WINDOW')
window.geometry('300x300')

# pack 放置方法
#tk.Label(window, text=6).pack(side='top')
#tk.Label(window, text=6).pack(side='left')
#tk.Label(window, text=6).pack(side='bottom')
#tk.Label(window, text=6).pack(side='right')

# grid 网格放置方法
#for i in range(3):
#    for l in range(4):
#        tk.Label(window, text=6).grid(row=i, column=l, padx=16, pady=16)

# place 放置方法（坐标精准定位）
tk.Label(window, text=6).place(x=50, y=150, anchor='nw')



window.mainloop()
