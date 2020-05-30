#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/30/2020 10:24 PM
# @Author : Tian Z
# @Site : 
# @File : 10-11_12.py
# @Software: PyCharm
# @Version:

import json

filename = "favorite_number.json"
try:
    with open(filename) as f_obj:
        favorite_num = json.load(f_obj)
except FileNotFoundError:
    with open(filename, "w") as f_obj:
        favorite_num = input("Please enter your favorite number: ")
        json.dump(favorite_num, f_obj)
        print("I'll remember your favorite number next time! It's " + favorite_num + '.')
else:
    print("I know your favorite number! It's " + favorite_num + '.')
