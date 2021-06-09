# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: rename_dir_test.py
@Create Time: 2021/6/7 10:16
"""
import os

test_string = "KG-DM00-0006-UF-KG"
split_str = test_string.split("-")
print(split_str)
print(split_str[-1])
split_str.insert(-1, "01")
print(split_str)
new_srt = "-".join(split_str)
print(new_srt)

print("*********")
test_string_2 = "KG-DM00-0006-UF-KG"
split_str_2 = test_string.split("-")
split_str_2.append("EF")
print(split_str_2)

path = input("Enter the path:")
for dir_name, sub_dirs, filenames in os.walk(path):
    print(dir_name)
    print(sub_dirs)
    print(filenames)

print("**********")
print(os.listdir(path))

test_string_3 = "KG-DM00-0006-UF-01-01.catpart"
verify_str = "-01-01"
print(verify_str in test_string_3)
if verify_str in test_string_3:
    test_string_3 = test_string_3.replace("-01-01", "-01-KG")
print(test_string_3)
