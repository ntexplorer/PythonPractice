# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: rename_data.py
@Create Time: 2021/6/7 15:57
"""

import pandas as pd

# Pandas读取excel，需要Openxlsx库
df = pd.read_excel('data/template_info.xlsx')


# 替换目录名
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


# 替换文件夹路径
def rename_path(path):
    # 用\分割文件夹路径（需转义）
    split_path = path.split("\\")
    # 将拆分后的末段（文件夹名）替换
    split_path[-1] = rename_dir(split_path[-1])
    # 合成新路径
    new_path = "\\".join(split_path)
    return new_path


def rename_file(filename):
    verify_str_list = ["-01-01", "-05-KG", "-05-PI", "-05-CE", "-05-UM"]
    replace_str_list = ["-01-KG", "-01-PI", "-01-CE", "-01-UM"]
    for verify_str in verify_str_list:
        if verify_str in filename:
            # 单次if循环读取列表中的不同元素判断替换条件
            if verify_str == verify_str_list[2]:
                new_filename = filename.replace(verify_str, replace_str_list[1])
            elif verify_str == verify_str_list[3]:
                new_filename = filename.replace(verify_str, replace_str_list[2])
            elif verify_str == verify_str_list[4]:
                new_filename = filename.replace(verify_str, replace_str_list[3])
            else:
                new_filename = filename.replace(verify_str, replace_str_list[0])
            return new_filename
        else:
            continue
    return filename


# apply函数调用函数至不同的列
df['template_number'] = df['template_number'].apply(rename_dir)
df['storage_file_path'] = df['storage_file_path'].apply(rename_path)
df['template_file_name'] = df['template_file_name'].apply(rename_file)
df['template_source_file_name'] = df['template_source_file_name'].apply(rename_file)

# 生成新excel表
df.to_excel('data/template_info_modified.xlsx')

input("数据替换完毕，按回车结束")
