#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 12:12
# @Author : Tian ZHANG
# @Site : 
# @File : dialog.py
# @Software: PyCharm
# @Version:

from tkinter import *
from tkinter.dialog import *


def dialog():
    d = Dialog(None, title='This is a dialog', text='Dialog test', bitmap=DIALOG_ICON, default=0,
               strings=('test1', 'test2', 'test3'))
    print(d.num)


t = Button(None, text='Test4', command=dialog)
t.pack()
b = Button(None, text='test5', command=t.quit)
b.pack()
t.mainloop()
