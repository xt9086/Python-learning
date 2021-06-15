#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""重写的字符串替换函数"""


# 1.自己想的方法，但是有bug，新旧字符串有重复部分会引起死循环
# def my_replace(whole_str, old_str, new_str):
#     """
#     把原字符串的部分内容替换，返回一个新的字符串
#     :param whole_str: 原字符串
#     :param old_str: 要被替换的字符串
#     :param new_str: 用来替换的新字符串
#     :return: 替换好的新字符串
#     """
#     len_old = len(old_str)
#     new_whole_str = whole_str[:]
#     while True:
#         if old_str not in new_whole_str:
#             print('没有要替换的地方了')
#             break
#         for i in range(len(new_whole_str) - len_old + 1):
#             if new_whole_str[i:i + len_old] == old_str:
#                 new_whole_str = new_whole_str[:i] + new_str + new_whole_str[i + len_old:]
#                 break
#     return new_whole_str

# 2.使用str类的split和join方法
# def my_replace(whole_str, old_str, new_str):
#     return new_str.join(whole_str.split(old_str))

# 3.使用while循环
def my_replace(whole_str, old_str, new_str):
    result = ''
    i = 0
    while i < len(whole_str):
        if whole_str[i:i + len(old_str)] != old_str:
            result += whole_str[i]
            i += 1
        else:
            result += new_str
            i += len(old_str)
    return result


if __name__ == '__main__':
    print(my_replace('hello world hello world', 'he', 'she'))
    # my_replace('hello world hello world', 'hello', 'hi')
    print()
