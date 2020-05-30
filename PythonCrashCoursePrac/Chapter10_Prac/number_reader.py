#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/30/2020 10:17 PM
# @Author : Tian Z
# @Site : 
# @File : number_reader.py
# @Software: PyCharm
# @Version:

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
