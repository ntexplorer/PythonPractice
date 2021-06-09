# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: add_image.py
@Create Time: 2021/6/9 9:52
"""

import os
import shutil


def copy_image(origin, target):
    # 复制计数
    copy_count = 0
    for dir_name, sub_dirs, filenames in os.walk(origin):
        for filename in filenames:
            # 拆分文件名，去除扩展名
            split_filename = filename.split(".")
            target_name = split_filename[0]
            for dir_name_2, sub_dirs_2, filenames_2 in os.walk(target):
                # 遍历模板文件夹
                for sub_dir_2 in sub_dirs_2:
                    if target_name == sub_dir_2:
                        # 图片名和目录名相同时，生成图片路径和文件夹路径
                        file_path = os.path.join(dir_name, filename)
                        target_path = os.path.join(dir_name_2, sub_dir_2)
                        # 拷贝图片至文件夹
                        shutil.copy(file_path, target_path)
                        print(filename + "已成功复制到" + target_path)
                        # 计数+1
                        copy_count += 1
                    else:
                        continue
    return copy_count


if __name__ == '__main__':
    origin_path = input("请输入图片文件夹绝对路径：")
    target_path = input("请输入目标文件夹绝对路径：")
    count = copy_image(origin_path, target_path)
    print("目录已复制完成，已成功复制", count, "个文件")
    input("回车键退出")
