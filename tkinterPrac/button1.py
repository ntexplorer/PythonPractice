#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 0:15
# @Author : Tian ZHANG
# @Site : 
# @File : button1.py
# @Software: PyCharm

from tkinter import *


def newlabel():
    global xin
    s = Label(xin, text='I love python')
    s.pack()


xin = Tk()
b1 = Button(xin, text="xin", command=newlabel)
b1.pack()

xin.mainloop()
