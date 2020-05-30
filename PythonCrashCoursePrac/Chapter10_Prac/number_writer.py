#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/30/2020 10:15 PM
# @Author : Tian Z
# @Site : 
# @File : number_writer.py
# @Software: PyCharm
# @Version:

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
