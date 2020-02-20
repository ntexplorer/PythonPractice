#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 0:19
# @Author : Tian ZHANG
# @Site : 
# @File : button2.py
# @Software: PyCharm

from tkinter import *


def newlabel(event):
    global xin
    s = Label(xin, text='I love python')
    s.pack()


xin = Tk()
b1 = Button(xin, text='xin')
b1.bind('<Button-1>', newlabel)
# <Button-1> for left click of the mouse
b1.bind('<Button-2>', newlabel)
# <Button-2> for click of the scroll
b1.pack()
xin.mainloop()
