#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""reduce函数易错点"""
from functools import reduce

L = [
    {'index': 0, 'data': 5},
    {'index': 1, 'data': 12},
    {'index': 2, 'data': 13}
]


def get_ele_sum(x, y):
    return x['data'] + y['data']


print(reduce(get_ele_sum, L))

# 结果会报错 TypeError: 'int' object is not subscriptable
# 原因是reduce会把get_ele_sum(x, y)返回的结果作为下一轮的参数x
# 但是L的元素都是字典，get_ele_sum(x, y)的返回值是整数
# 接着整数x传入函数计算x['data'] + y['data']就会出错，因为整数没有下标

#   解决方法一
# 使参数一函数的返回值和参数二列表里的元素类型保持一致

#   解决方法二
# reduce还可以接收一个初始化参数，把它添加到第二个参数的序列最前面参与第一次运算
# 去掉函数get_ele_sum内参数一的下标
# 给reduce加个个初始化值参数0
# 这个0相当于加在L的第一个元素，除了第一次x等于0
# 以后x都是等于y['data']然后和下一个y['data']相加
# def get_ele_sum(x, y):
#     return x + y['data']
#
#
# print(reduce(get_ele_sum, L, 0))
