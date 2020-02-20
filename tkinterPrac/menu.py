#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 11:17
# @Author : Tian ZHANG
# @Site : 
# @File : menu.py
# @Software: PyCharm
# @Version:

from tkinter import *

root = Tk()
menubar = Menu(root)

fmenu = Menu(menubar)
for item in ['New', 'Open', 'Save', 'Save as']:
    fmenu.add_cascade(label=item)

emenu = Menu(menubar)
for item in ['Copy', 'Paste', 'Cut']:
    emenu.add_cascade(label=item)

vmenu = Menu(menubar)
for item in ['Default View', 'New View']:
    vmenu.add_cascade(label=item)

amenu = Menu(menubar)
for item in ['Copyright', 'Statement']:
    amenu.add_cascade(label=item)

menubar.add_cascade(label='File', menu=fmenu)
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='View', menu=vmenu)
menubar.add_cascade(label='About', menu=amenu)
root['menu'] = menubar
root.mainloop()
