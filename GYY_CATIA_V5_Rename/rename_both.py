# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: rename_both.py
@Create Time: 2021/6/4 14:50
"""

import os


def rename_dir(path):
    existing_count = 0
    rename_count = 0
    for dir_name, sub_dirs, filenames in os.walk(path):
        for sub_dir in sub_dirs:
            try:
                split_dir = sub_dir.split("-")
                if len(split_dir) == 5 and split_dir[-1] == "KG":
                    split_dir.insert(-1, "01")
                    new_dir = "-".join(split_dir)
                    os.rename(os.path.join(dir_name, sub_dir),
                              os.path.join(dir_name, new_dir))
                    rename_count += 1
                    print(sub_dir + "文件夹已成功重命名，新名称为：" + new_dir)
                elif len(split_dir) == 5 and split_dir[-1] == "01":
                    split_dir.append("KG")
                    new_dir = "-".join(split_dir)
                    os.rename(os.path.join(dir_name, sub_dir),
                              os.path.join(dir_name, new_dir))
                    rename_count += 1
                    print(sub_dir + "文件夹已成功重命名，新名称为：" + new_dir)
                else:
                    continue
            except FileExistsError:
                existing_count += 1
                print(existing_count, "个文件夹已存在，已保留原文件夹")
    return [rename_count, existing_count]


def rename_file(path):
    rename_count_2 = 0
    verify_str = "-01-01"
    replace_str = "-01-KG"
    for dir_name, sub_dirs, filenames in os.walk(path):
        for filename in filenames:
            if verify_str in filename:
                new_filename = filename.replace(verify_str, replace_str)
                os.rename(os.path.join(dir_name, filename),
                          os.path.join(dir_name, new_filename))
                rename_count_2 += 1
                print(filename + "文件已成功重命名，新名称为：" + new_filename)
            else:
                continue
    return rename_count_2


if __name__ == '__main__':
    path_name = input("请输入根目录绝对路径：")
    list_1 = rename_dir(path_name)
    num_1 = rename_file(path_name)
    print("转换完成！已重命名", list_1[0], "个文件夹，其中", list_1[1], "个文件夹已存在")
    print("转换完成！已重命名", num_1, "个文件")
    input("回车键退出")
