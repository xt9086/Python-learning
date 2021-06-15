#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" 实现计数器统计函数调用次数 """


# def create_counter():
#     """方法1
#     list是可变类型，在其它地方改变list里的值
#     会影响到所有指向该list的变量
#     """
#     num = [0]
#
#     def counter():
#         num[0] += 1
#         return num[0]
#
#     return counter

# n = 0
#
#
# def create_counter():
#     """方法2
#     使用global声明n为全局变量
#     """
#     global n
#     n = 0
#
#     def counter():
#         global n
#         n += 1
#         return n
#
#     return counter


# def create_counter():
#     """方法3
#     使用nonlocal声明内层函数变量n
#     使其能修改除全局变量外的外层函数的变量
#     """
#     n = 0
#
#     def counter():
#         nonlocal n
#         n += 1
#         return n
#
#     return counter


def create_counter():
    """方法4
    使用生成器在外层函数创建生成器对象，在内层函数调用next()
    """

    def count_generator():
        n = 0
        while True:
            n += 1
            yield n

    # 调用生成器函数创建生成器对象一定要在外层函数进行
    # 否则每次调用内层函数都会创建一个新的生成器从头开始计数
    temp = count_generator()

    def get_num():
        return next(temp)

    return get_num


if __name__ == '__main__':
    # 测试:
    counterA = create_counter()
    # 调用create_counter()返回的是未调用的内层函数
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = create_counter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
