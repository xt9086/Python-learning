#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""求斐波那契数列第n项"""


#   1.循环法之一
# def fb(n):
#     if n < 3:
#         return 1
#     else:
#         f1 = f2 = 1
#         for i in range(n - 2):
#             # f1、f2是相邻的前后两项，用中间变量保存初始位置的值
#             temp = f1
#             # 将旧的后一项换到移动一位后新的前一项的位置
#             f1 = f2
#             # 新的后一项值等于原来两项之和
#             f2 = temp + f1
#         return f2

# 2.循环法之二
def fb(n):
    f1 = 0
    # f1置零为了将数列前移一位
    f2 = 1
    count = 0
    while count < n:
        count += 1
        # 拆包分散赋值实现交换
        f1, f2 = f2, f1 + f2
    return f1


#   3.递归法
# def fb(n):
#     if n <= 2:
#         return 1
#     return fb(n - 1) + fb(n - 2)


if __name__ == "__main__":
    num = int(input("请输入一个正整数："))
    print('斐波那契数列第{0}项是{1}'.format(num, fb(num)))
    # print(fb(6))
