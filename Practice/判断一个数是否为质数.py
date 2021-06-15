#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""判断一个数是否为质数"""

num = int(input("请输入一个正整数："))
if num < 2:
    print(num, "不是质数")
for m in range(2, num):
    # 优化方向
    # 1. range(2, num)改为range(2, int(num**0.5)+1)
    # 假如一个数N是合数,它有一个约数a,那么有a×b=N
    # 则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N。
    # 因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数
    # 2. 可以先筛选掉比如偶数，3、5、7等的倍数
    if num % m == 0:
        print(num, "不是质数")
        break
else:
    # for...else...当for语句下的break不执行时才执行else下内容
    print(num, "是质数")

    # 7~20行其他实现方法

#   1. 计数法
#     count = 0
# for m in range(2, num):
#     if num % m == 0:
#         print(num, "不是质数")
#         # count记录被整除的次数
#         count+=1
#         break
#
# if count == 0:
#     print("是质数")
# else:
#     print("不是质数")

#   2.布尔值标志法
# flag = True
# for m in range(2, num):
#     if num % m == 0:
#         print(num, "不是质数")
#         # flag标志为False表示被整除过
#         flag = False
#         break
#
# if flag:
#     print("是质数")
# else:
#     print("不是质数")
