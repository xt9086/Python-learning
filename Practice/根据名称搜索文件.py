#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""根据字符串搜索指定路径下所有的文件夹和文件"""
import os


def filename_search(matching_str, start_path, path_list=None):
    """
    递归搜索指定路径下所有含有该字符串的文件夹或文件
    并打印搜索到的对象的绝对路径
    若给出的是当前路径'.',那么打印的是相对路径
    :param matching_str: 用于搜索匹配的字符串
    :param start_path: 搜索起始路径
    :param path_list: 默认为None，用来保存搜索结果
    :return: 搜索结果path_list
    """
    # 增加参数path_list是为了能保存搜索结果
    # 以免在递归中每次被重新初始化赋值
    # path_list默认为不可变对象None而不是可变的空列表[]
    # 是为了防止多次调用函数且缺省默认参数path_list时被前面结果影响
    if path_list is None:
        path_list = []
    if os.path.isdir(start_path):
        # 是文件夹才查找其子目录
        addr_list = os.listdir(start_path)
        for addr in addr_list:
            # 遍历子目录，将匹配的结果组合成路径打印并保存
            if matching_str in addr:
                result = os.path.join(start_path, addr)
                print(result)
                path_list.append(result)
        # 先查找本层目录输出匹配的结果，再递归查找子文件夹
        for filename in addr_list:
            filename_search(matching_str, os.path.join(start_path, filename), path_list=path_list)
    return path_list


if __name__ == '__main__':
    s = '.py'
    address = r'C:\Users\xt908\Desktop\test'
    print(filename_search(s, address))
