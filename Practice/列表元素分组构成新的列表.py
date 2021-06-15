#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""将列表里的元素每三个组成一个列表，再由这些列表组成一个新的列表"""

L1 = list(range(1, 101))

#   1.常规方法
# L2 = []
# L3 = []
# k = 0
# for i in L1:
#     k += 1
#     L2.append(i)
#     if k % 3 == 0:
#         L3.append(L2[::])
#         # 若使用L3.append(L2),当L2.clear()执行时，L3里的L2也会被删除
#         # 而L2[::]是L2的一个副本，内存地址不一样，L2的改变不会影响到它
#         L2.clear()
# while L2 and len(L2) != 3:
#     # 当L1的元素个数不是三的倍数时，最后会剩len(L1)%3个元素在L2里
#     # L2不足三个元素时用空字符串补足三个元素
#     L2.append('')
# # 将凑齐的最后一组添加到L3
# L3.append(L2[::])
# print(L3)


#   2.使用列表推导式
group = [L1[j:j + 3] for j in range(0, 100, 3)]
# 对L1进行每次三个元素的切片，j取自range函数生成的0开始步长为3的数列
# 故j可取[0,3,6,...,99],切片位置也随j每次移动三个单位
while len(group[-1]) != 3:
    # 当最后一个列表元素不是3个时，用空字符串将其补齐
    group[-1].append('')
print(group)
