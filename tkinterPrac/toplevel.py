#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 12:34
# @Author : Tian ZHANG
# @Site : 
# @File : toplevel.py
# @Software: PyCharm
# @Version:

from tkinter import *

root = Tk()
root.title('This is a window for root')
l = Label(root, text='This one belongs to root', width=40, height=20)
l.pack()
f = Toplevel(root)
f.title('This is a toplevel')
lf = Label(f, text='this belongs to toplevel', width=40, height=40)
lf.pack()
root.mainloop()
