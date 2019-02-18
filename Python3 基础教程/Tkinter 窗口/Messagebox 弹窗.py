# 按钮点击触发的弹窗

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('WINDOW')
window.geometry('300x300')

def hit():
    # messagebox.showinfo(title='hi', message='111111')
    # messagebox.showwarning(title='hi', message='111111')
    # messagebox.showerror(title='hi', message='111111')
    # print(messagebox.askquestion(title='hi', message='111111'))# askquestion 返回 yes & no
    # print(messagebox.askyesno(title='hi', message='111111'))# askyesno 返回 true & false
    # print(messagebox.askokcancel(title='hi', message='111111'))# askokcancel 返回 true & false
    print(messagebox.askyesnocancel(title='hi', message='111111'))  # askquestion 返回 true & false & none

tk.Button(window, text='hit', command=hit).pack()

window.mainloop()