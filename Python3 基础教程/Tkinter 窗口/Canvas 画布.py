

import tkinter as tk

window = tk.Tk()
window.title('MY')
window.geometry('500x500')

canvas = tk.Canvas(window, bg='green', width=500, heigh=400)
image_file = tk.PhotoImage(file='welcome.gif')
# 将图片放到画布中前两个参数是对画布坐标0,0的偏差值，画布默认左上角0,0
# anchor 指的是图片的基准点在图片的什么位置，有nw，e，w，center等参数就是图片的各个角边
image = canvas.create_image(6, 6, anchor='nw',image=image_file)
x0, y0, x1, y1 = 200, 300, 300, 380
# 创建一条直线
line = canvas.create_line(x0, y0, x1, y1)
# 创建一个圆
oval = canvas.create_oval(x0, y0, x1, y1, fill='blue')
# 创建一个扇形
arc = canvas.create_arc(x0+100, y0, x1+100, y1, start=0, extent=180, fill='red')
# 创建一个长方形
rant = canvas.create_rectangle(x0-100, y0, x1-100, y1, fill='yellow')
canvas.pack()

def move_it():
    # 移动画布上已有的元素，0是x方向上，-6是y方向上
    canvas.move(arc, 0, -6)

b = tk.Button(window, text='move', command=move_it).pack()


window.mainloop()