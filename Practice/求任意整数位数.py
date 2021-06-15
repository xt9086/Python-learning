#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""求一个整数的位数"""

num = int((input('请输入一个整数：')))
i = 0
# 位数与正负无关，故如果是负数就转换成正数
m = num if num >= 0 else -num
while True:
    # 整除10到0为止，除的次数就是m的位数
    m = m // 10
    i += 1
    if m == 0:
        break
print(num, '是', i, '位数')
