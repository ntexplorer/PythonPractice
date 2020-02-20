#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 11:50
# @Author : Tian ZHANG
# @Site : 
# @File : menu2.py
# @Software: PyCharm
# @Version:

from tkinter import *


def printLove():
    global root
    Label(root, text='I love python').pack()


root = Tk()
menubar = Menu(root)

for x in ['vb', 'c', 'java', 'php']:
    menubar.add_command(label=x)

menubar.add_command(label='python', command=printLove)

menubar.add_separator()
for item in ['ruby', "c++"]:
    menubar.add_command(label=item)


def pop(event):
    menubar.post(event.x_root, event.y_root)


root.bind("<Button-3>", pop)

root.mainloop()
