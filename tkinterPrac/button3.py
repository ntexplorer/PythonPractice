#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 0:25
# @Author : Tian ZHANG
# @Site : 
# @File : button3.py
# @Software: PyCharm

from tkinter import *

xin = Tk()
b1 = Button(xin, text='xin')
b1['width'] = 20
b1['height'] = 4
b1.pack()
b2 = Button(xin, text='hello')
b2['width'] = 30
b2['background'] = 'yellow'
b2.pack()
xin.mainloop()
