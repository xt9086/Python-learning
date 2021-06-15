#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""冒泡排序"""

L = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2]
#   1.使用内置函数min()或者max()

# L_sorted = []
# for i in range(len(L)-1):
#     # 每循环一次都找出当前L的最小值
#     m = min(L)
#     # 将此轮最小值m添加到新的列表
#     L_sorted.append(m)
#     # 将此轮最小值m从L删除，以便下一轮求新的L的最小值
#     L.remove(m)
# L_sorted.append(L[0])
# print(L_sorted)

#   2.经典交换位置实现冒泡排序
for i in range(len(L)-1):
    tag = True
    for j in range(len(L)-1 - i):
        # 若前者比后者大，则交换位置，当此轮循环结束，最大值处在末端
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            tag = False
    # 优化：当tag为True说明上一趟内层循环的比较没有进行换位
    # 即剩下的元素本就是排序好的，无需再进行循环比较，退出循环
    if tag:
        break
print(L)
