#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 12:25
# @Author : Tian ZHANG
# @Site : 
# @File : checkbutton.py
# @Software: PyCharm
# @Version:

from tkinter import *

time1 = 0
time2 = 0


def checkbox1():
    global c1, time1
    if time1 % 2 == 0:
        time1 += 1
        l['text'] = 'checkbox1 selected'
    else:
        time1 += 1
        l['text'] = 'checkbox1 canceled'


def checkbox2():
    global c2, time2
    if time2 % 2 == 0:
        time2 += 1
        l['text'] = 'checkbox2 selected'
    else:
        time2 += 1
        l['text'] = 'checkbox2 canceled'


root = Tk()
c1 = Checkbutton(root, text='checkbox1', command=checkbox1)
c2 = Checkbutton(root, text='checkbox2', command=checkbox2)
c1.pack()
c2.pack()

l = Label(root, text='')
l.pack()
root.mainloop()
