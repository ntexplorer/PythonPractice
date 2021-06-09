# -*- coding:utf-8 _*-
"""
@Author:Tian Zhang
@File: image_check.py
@Create Time: 2021/6/9 11:02
"""

import os


def image_check(path):
    # 缺失计数
    missing_count = 0
    # 新建txt，写入首句
    with open("log.txt", "w") as f:
        f.write("缺失KG结尾图片的文件夹：\n")
    for dir_name, sub_dirs, filenames in os.walk(path):
        for sub_dir in sub_dirs:
            # 忽略父级文件夹
            if sub_dir[0] == "m":
                continue
            else:
                # 生成模板文件夹路径
                dir_path = os.path.join(dir_name, sub_dir)
                # 生成图片名
                valid_name = sub_dir + ".jpg"
                for dir_name_2, sub_dirs_2, filenames_2 in os.walk(dir_path):
                    # 模板文件夹中无同名图片
                    if valid_name not in filenames_2:
                        # 计数+1
                        missing_count += 1
                        # append模式写入缺失数据
                        with open("log.txt", "a") as f:
                            f.write(dir_path + "\\" + valid_name + "\n")
    # 统计缺失数据，尾行添加
    with open("log.txt", "a") as f:
        f.write("共缺失" + str(missing_count) + "个文件\n")
    return missing_count


if __name__ == '__main__':
    target_path = input("请输入文件夹绝对路径：")
    count = image_check(target_path)
    print("目录已检查完毕，共缺失", count, "个文件")
