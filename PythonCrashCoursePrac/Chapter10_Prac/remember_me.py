#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/30/2020 10:20 PM
# @Author : Tian Z
# @Site : 
# @File : remember_me.py
# @Software: PyCharm
# @Version:

import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
