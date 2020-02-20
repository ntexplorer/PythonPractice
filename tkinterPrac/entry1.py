#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 0:31
# @Author : Tian ZHANG
# @Site : 
# @File : entry1.py
# @Software: PyCharm

from tkinter import *

window = Tk()
Label(window, text='Username').grid(row=0, sticky=W)
Entry(window).grid(row=0, column=1, sticky=E)

Label(window, text='Password').grid(row=1, sticky=W)
Entry(window).grid(row=1, column=1, sticky=E)

Button(window, text='Login').grid(row=2, column=1, sticky=W)
window.mainloop()
