#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from functools import reduce


def str2float(s: str):
    """
    去掉小数点，拼接成新的字符串
    将新字符串转为大整数，再将该整数除以10**len(point_right)
    len(point_right)是指原字符串小数点右边的位数
    :param s: 待转换的字符串
    :return: 转换好的对应浮点数
    """
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    point_left, point_right = s.split('.')
    new_str = point_left + point_right

    def char2num(char):
        return digits[char]

    return reduce(lambda x, y: x * 10 + y, map(char2num, new_str)) / 10**len(point_right)


if __name__ == '__main__':
    print(str2float('12345.6789'))
