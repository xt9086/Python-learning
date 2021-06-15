#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""求列表里的的最大与最小值"""


def find_max_min(num_list):
    """
    接收一个数字列表，返回其中的最大值与最小值
    :param num_list: 数字列表
    :return: 最大值与最小值组成的元组
    """
    if not num_list:
        # 若列表为空，返回None
        return None
    max_num = num_list[0]
    # 设列表里第一个元素为初始值，便于按顺序与后面的元素逐一比较
    min_num = num_list[0]
    for num in num_list[1:]:
        if num > max_num:
            # 若比默认最大值还大就设它为新的最大值
            max_num = num
        if num < min_num:
            # 若比默认最小值还小就设它为新的最小值
            min_num = num
    return max_num, min_num


if __name__ == '__main__':
    # 测试
    l1 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_max_min(l1), find_max_min([]))
