#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""九九乘法表"""

#   1.while循环写法
m = 0
while m < 9:  # 行数
    m += 1
    n = 0
    while n < m:  # 每一行多少列
        n += 1
        print(n, '*', m, '=', n * m, end='\t')
    print()

#   2.for循环写法
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, '*', i, '=', j * i, end='\t')
#     print()
