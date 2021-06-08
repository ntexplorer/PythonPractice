# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: rename_data.py
@Create Time: 2021/6/7 15:57
"""

import pandas as pd

df = pd.read_excel('data/template_info.xlsx')


def rename_dir(directory):
    split_dir = directory.split("-")
    if len(split_dir) == 5 and split_dir[-1] == "KG":
        split_dir.insert(-1, "01")
        new_dir = "-".join(split_dir)
        return new_dir
    elif len(split_dir) == 5 and split_dir[-1] == "01":
        split_dir.append("KG")
        new_dir = "-".join(split_dir)
        return new_dir
    else:
        return directory


def rename_path(path):
    split_path = path.split("\\")
    split_path[-1] = rename_dir(split_path[-1])
    new_path = "\\".join(split_path)
    return new_path


def rename_file(filename):
    verify_str = "-01-01"
    replace_str = "-01-KG"
    if verify_str in filename:
        new_filename = filename.replace(verify_str, replace_str)
        return new_filename
    else:
        return filename


df['template_number'] = df['template_number'].apply(rename_dir)
df['storage_file_path'] = df['storage_file_path'].apply(rename_path)
df['template_file_name'] = df['template_file_name'].apply(rename_file)
df['template_source_file_name'] = df['template_source_file_name'].apply(rename_file)

df.to_excel('data/template_info_modified.xlsx')

input("数据替换完毕，按回车结束")
