#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
root = Tk()
root.title('画板')
Label(root, text='画笔粗细:').pack()
r = StringVar()
r.set('1')
size = Spinbox(root, textvariable=r, value=('2', '5', '10', '15', '20'))
size.pack()
c = StringVar()
c.set('red')
Label(root, text='画笔颜色:').pack()
color = OptionMenu(root, c, 'red', 'black', 'blue', 'yellow', 'green')
color.pack()
w = Canvas(root, width=1000, height=500, background='white')
w.pack()



def paint(event):
    r = int(size.get())
    x1, y1 = (event.x-r), (event.y-r)
    x2, y2 = (event.x+r), (event.y+r)
    w.create_oval(x1, y1, x2, y2, outline=c.get(), fill=c.get())


def clear():
    w.delete(ALL)
Button(root, text='清除', command=clear).pack(side=RIGHT)
w.bind("<B1-Motion>", paint)
Label(root, text='按住鼠标左键并移动，开始绘制你的图吧').pack()
mainloop()
