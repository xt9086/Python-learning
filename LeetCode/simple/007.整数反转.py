#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
"""


# 方法1.转字符串逆序再转回整数
# def reverse(x: int) -> int:
#     if 0 <= x <= 11:
#         return x
#     elif x < 0:
#         result = -int(str(-x).rstrip('0')[::-1])
#     else:
#         result = int(str(x).rstrip('0')[::-1])
#     if -2 ** 31 <= result <= 2 ** 31 - 1:
#         return result
#     else:
#         return 0

# 方法2.数学公式法
def reverse(x: int) -> int:
    if x >= 0:
        # 符号标志
        sign = 1
    else:
        x = -x
        sign = -1
    r = 0
    # 前面将x转成x的绝对值并且设了符号位，故下面只用处理非负整数的情况
    while x:
        x, m = x // 10, x % 10
        r = r * 10 + m
    # 使用二进制移位运算提高运算速度，注意移位运算符的优先级
    if -(1 << 31) <= r <= ((1 << 31) - 1):
        return r * sign
    else:
        return 0


# 方法3.方法2的另一种写法
# def reverse(x: int) -> int:
#     """提前分类讨论x的符号和对应边界值"""
#     if x >= 0:
#         # 符号标志
#         sign = 1
#         # 提前计算好的边界值
#         boundary = 2147483647  # 2**31-1
#     else:
#         x = -x
#         sign = -1
#         boundary = 2147483648  # 2**31
#     r = 0
#     # 只用处理x非负的情况，结果的符号由sign决定
#     while x:
#         x, m = x // 10, x % 10
#         r = r * 10 + m
#         # 提前判断是否越界
#         if r > boundary:
#             return 0
#     return r * sign


if __name__ == '__main__':
    # 测试
    test_cases = [0, 123, -123, -12300, -2147483412, 1463847412, 2 ** 32, -2 ** 32]
    expectation = [0, 321, -321, -321, -2143847412, 2147483641, 0, 0, ]
    result_list = []
    for case in test_cases:
        result_list.append(reverse(case))
    print(result_list)
    assert result_list == expectation
