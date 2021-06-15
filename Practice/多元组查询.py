#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""跨三个元组进行查询"""

t1 = (0, 1, 2, 3, 4)
t2 = (1, 3, 5, 7, 9)
t3 = (1, 2, 4, 6, 8)

#   1.求共有多少不同的数字
# t = t1 + t2 + t3
# l1 = []
# k = 0
# for i in t:
#     if i not in l1:
#         l1.append(i)
#         k += 1
# print(k)

#   2.求只在t1有的数字有哪些，共多少个
# t = t2 + t3
# m = 0
# print('只在t1有的数字是：', end='')
# for num in t1:
#     if num not in t:
#         m += 1
#         print(num, end=',')
# print(f'共{m}个')

#   3.求只在其中1/2/3个元组的数字有哪些，多少个
from 获取列表中每个元素出现的次数 import count_elements

dt = count_elements(list(t1 + t2 + t3))
l1 = []
l2 = []
l3 = []
# 求出所有元素的次数，再找次数为1/2/3的元素
for k, v in dt.items():
    if v == 1:
        l1.append(k)
    elif v == 2:
        l2.append(k)
    elif v == 3:
        l3.append(k)
print('1个：', l1, ',', len(l1))
print('2个：', l2, ',', len(l2))
print('3个：', l3, ',', len(l3))
