# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: rename_both.py
@Create Time: 2021/6/4 14:50
"""

import os


def rename_dir(path):
    # 重命名计数、删除文件夹计数
    rename_count = 0
    dir_deletion_count = 0
    for dir_name, sub_dirs, filenames in os.walk(path):
        # 遍历目标文件夹
        for sub_dir in sub_dirs:
            try:
                # 用”-“拆分文件夹名
                split_dir = sub_dir.split("-")
                # 条件1，文件夹名由5段且KG结尾
                if len(split_dir) == 5 and split_dir[-1] == "KG":
                    # 倒数第二段插入01
                    split_dir.insert(-1, "01")
                    # 生成新文件夹名
                    new_dir = "-".join(split_dir)
                    # 重命名文件夹
                    os.rename(os.path.join(dir_name, sub_dir),
                              os.path.join(dir_name, new_dir))
                    # 重命名计数+1
                    rename_count += 1
                    print(sub_dir + "文件夹已成功重命名，新名称为：" + new_dir)
                # 条件2，文件夹名由5段且01结尾
                elif len(split_dir) == 5 and split_dir[-1] == "01":
                    # 末段加KG
                    split_dir.append("KG")
                    new_dir = "-".join(split_dir)
                    os.rename(os.path.join(dir_name, sub_dir),
                              os.path.join(dir_name, new_dir))
                    rename_count += 1
                    print(sub_dir + "文件夹已成功重命名，新名称为：" + new_dir)
                else:
                    # 其余情况继续循环
                    continue
            # 重复文件夹处理
            except FileExistsError:
                # 先组成要删除的文件夹路径
                delete_dir_path = os.path.join(dir_name, sub_dir)
                # print(delete_dir_path)
                # 调用删除函数删除文件夹内所有文件（不能删除不为空的文件夹）
                delete_file(delete_dir_path)
                # 文件夹为空后进行删除
                os.rmdir(delete_dir_path)
                # 文件夹删除计数+1
                dir_deletion_count += 1
                print(sub_dir, "文件夹已存在，已清空并删除重复文件夹")
    # 返回计数列表
    return [rename_count, dir_deletion_count]


# 清空文件夹函数
def delete_file(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        # 是文件就删除，不是文件就递归
        if os.path.isfile(file_data):
            os.remove(file_data)
            print(file_data, "文件重复，已删除")
        else:
            delete_file(file_data)


def rename_file(path):
    # 添加重命名计数、删除文件计数
    rename_count_2 = 0
    file_deletion_count = 0
    # 针对不同规则设置不同替换列表
    verify_str_list_1 = ["-01-01", "-01-KG-SK", "-5.0-KG", "-1.0-KG", "-05-KG", "--KG"]
    verify_str_list_2 = ["--PI", "-05-PI"]
    verify_str_list_3 = ["--CE", "-1.0-CE", "-05-CE"]
    verify_str_list_4 = ["--UM", "-1.0-UM", "-05-UM"]
    replace_str_1 = "-01-KG"
    replace_str_2 = "-01-PI"
    replace_str_3 = "-01-CE"
    replace_str_4 = "-01-UM"
    for dir_name, sub_dirs, filenames in os.walk(path):
        for filename in filenames:
            # 调用文件处理函数，对文件名进行审阅
            ls_1 = file_process(verify_str_list_1, dir_name, filename, replace_str_1)
            ls_2 = file_process(verify_str_list_2, dir_name, filename, replace_str_2)
            ls_3 = file_process(verify_str_list_3, dir_name, filename, replace_str_3)
            ls_4 = file_process(verify_str_list_4, dir_name, filename, replace_str_4)
            # 每遍历一个文件就添加一次计数
            rename_count_2 += (ls_1[0] + ls_2[0] + ls_3[0] + ls_4[0])
            file_deletion_count += (ls_1[1] + ls_2[1] + ls_3[1] + ls_4[1])
    # 返回计数列表
    return [rename_count_2, file_deletion_count]


def file_process(verify_str_list, dir_name, filename, replace_str):
    rename_count_2 = 0
    file_deletion_count = 0
    for verify_str in verify_str_list:
        try:
            # 如文件名中包含验证字段
            if verify_str in filename:
                # 将验证字段替换为替换字段
                new_filename = filename.replace(verify_str, replace_str)
                os.rename(os.path.join(dir_name, filename),
                          os.path.join(dir_name, new_filename))
                rename_count_2 += 1
                print(filename + "文件已成功重命名，新名称为：" + new_filename)
            else:
                continue
        # 如文件名重命名后已存在
        except FileExistsError:
            # 删除此文件
            os.remove(os.path.join(dir_name, filename))
            file_deletion_count += 1
            print(filename + "更名后存在重复文件，已删除")
    return [rename_count_2, file_deletion_count]


if __name__ == '__main__':
    path_name = input("请输入根目录绝对路径：")
    # 用两个列表存储最终计数
    list_1 = rename_dir(path_name)
    list_2 = rename_file(path_name)
    print("转换完成！已重命名", list_1[0], "个文件夹，其中", list_1[1], "个文件夹重复，已进行删除操作")
    print("转换完成！已重命名", list_2[0], "个文件，其中", list_2[1], "个文件重命名后重复，已进行删除操作")
    input("回车键退出")
