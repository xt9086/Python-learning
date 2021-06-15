#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" 三种方法实现计算x的n次方 """


def power1(x, n):
    """ 循环 """
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def power2(x, n):
    """ 递归 """
    if n == 0:
        return 1
    return x * power2(x, n - 1)


def power3(x, n):
    """ 尾递归 """
    return power_temp(x, n, 1)  # s初值置1


def power_temp(x, n, s):
    # 尾递归只可返回函数本身不能附加表达式
    # 所以多引入一个参数s来参加累乘
    # 每一层递归x累乘一次
    # n减至0时返回s的值
    if n == 0:
        return s
    return power_temp(x, n - 1, s * x)


if __name__ == "__main__":
    print(power1(2, 10))
    print(power2(2, 9))
    print(power3(2, 8))
