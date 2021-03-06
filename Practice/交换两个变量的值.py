#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""交换两个变量的值"""
a = a0 = 1
b = b0 = 2

#   1.引入中间变量
t = a
# 在a被新的赋值覆盖前，将原来的a值暂存在中间变量t
a = b
# 将b的值赋给a
b = t
# b的值被中间变量t存的原来a的值给覆盖

#   2.利用分散赋值
# a, b = b, a
# # 原式相当于a,b=(a,b)，右边的是一个元组
# # 在赋值时拆包，将元组里元素的值逐一覆给变量
# # 这一过程本质上是将左边变量指向右边元组元素对应的内存地址
# # 并且元组里的元素a,b与原来的变量a,b值相同，但内存地址不同
# # 所以元组里的值不会因交叉赋值而改变，相当于是原来a,b值的副本
# # 原式等效于以下代码：
# # t = (a, b)
# # a = t[1]
# # b = t[0]

#   3.使用异或运算符
# a = a ^ b
# # 由异或运算的特性可知：a^b^b=a,b^a^a=b
# b = a ^ b
# # b=a^b=a0^b0^b0=a0=1
# a = a ^ b
# # a=a^b=(a0 ^ b0) ^ (a0 ^ b0 ^ b0)=(a0 ^ b0)^a0=b0=2

print('a=', a, 'b=', b)
