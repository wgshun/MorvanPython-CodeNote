# 登录窗口 欢迎图片，输入账号密码，登陆注册按钮

import tkinter as tk

# 设置登录窗口信息
window = tk.Tk()
window.title('Tkinter 登录窗口')
window.geometry('500x350')

# 使用canvas画布放置欢迎语图片
canvas = tk.Canvas(window, width=440, heigh=160)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack()

# 设置账号密码登陆注册等信息
tk.Label(window, text='账号:', font=16).place(x=150, y=180)
tk.Label(window, text='密码:', font=16).place(x=150, y=210)
username = tk.StringVar()
# username.set('123@163.com')# 默认显示
password = tk.StringVar()
tk.Entry(window, textvariable=username).place(x=210, y=180)
tk.Entry(window, textvariable=password, show='*').place(x=210, y=210)

# 登陆与注册两个函数
import pickle # pickle库用来保存数据的一个模块
from tkinter import messagebox
def login():
    user_name = username.get()
    pass_word = password.get()
    try:
        with open('user_info.pickle', 'rb') as user_file:# 使用open打开pickle文件
            user_info = pickle.load(user_file) # 使用load加载pickle文件
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file:
            user_info = {'admin':'admin'}
            pickle.dump(user_info, user_file) # 使用dump保存pickle文件
    if user_name in user_info:
        if pass_word == user_info[user_name]:
            messagebox.showinfo(title='欢迎登录!', message='登录成功。')
        else:
            messagebox.showerror(title='登录错误!', message='密码不正确，请重新输入.')
    else:
        re = messagebox.askyesno(title='登录错误!', message='账号不存在，是否注册账号？')
        if re == True:
            sign()
        else:
            pass

def sign():
    def sign_up():
        user_name = username.get()
        pass_word = password.get()
        repass_word = repassword.get()
        if pass_word == repass_word:
            with open('user_info.pickle', 'rb') as user_file:
                user_info = pickle.load(user_file)
            if user_name in user_info:
                messagebox.showwarning(title='错误!', message='账号已存在，请重新输入.')
            else:
                with open('user_info.pickle', 'wb') as user_file:
                    newus = {user_name: pass_word}
                    pickle.dump(newus, user_file)
                messagebox.showinfo(title='注册!', message='注册成功。')
                window_sign.destroy()

        else:
            messagebox.showwarning(title='错误!', message='两次密码不一致，请重新输入.')
    # 用户注册界面
    window_sign = tk.Toplevel(window)
    window_sign.title('用户注册')
    window_sign.geometry('400x300')
    tk.Label(window_sign, text='请输入您的账号:', font=16).place(x=50, y=50)
    tk.Label(window_sign, text='请输入您的密码:', font=16).place(x=50, y=90)
    tk.Label(window_sign, text='请重复您的密码:', font=16).place(x=50, y=130)
    username = tk.StringVar()
    password = tk.StringVar()
    repassword = tk.StringVar()
    tk.Entry(window_sign, textvariable=username).place(x=180, y=50)
    tk.Entry(window_sign, textvariable=password, show='*').place(x=180, y=90)
    tk.Entry(window_sign, textvariable=repassword, show='*').place(x=180, y=130)
    tk.Button(window_sign, text='确定', command=sign_up).place(x=190, y=160)
    tk.Button(window_sign, text='返回', command=window_sign.destroy).place(x=250, y=160)
    window_sign.mainloop()

tk.Button(window, text='登录', command=login).place(x=210, y=250)
tk.Button(window, text='注册', command=sign).place(x=280, y=250)

window.mainloop()