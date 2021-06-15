#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""使用filter、lambda表达式与闭包的易错点"""


#   1.正确使用的情况

def not_equal(n):
    """
    绑定参数n，返回一个函数
    两个对象不相等则内层函数返回True
    """

    def lambda_func(x):
        print(f'被filter调用了，x={x},n={n}')
        return x != n

    # 相当于return lambda x : x != n
    return lambda_func


def correct_way():
    """正确的方式
    用于从序列中筛选掉指定内容并打印新序列
    """
    # 生成1,2,3,4,5,6的生成器
    g1 = (x for x in range(1, 7))
    for i in [1, 3, 5]:
        # 从g1过滤掉1,3,5
        g1 = filter(not_equal(i), g1)
        # 上一行等价于：g1 = filter(lambda x, m=i: x != m, g1)
    print(list(g1))


correct_way()

print("========分割线========")


#   2.错误使用的情况

def wrong_way():
    """错误的方式"""
    g2 = (x for x in range(1, 7))
    for i in [1, 3, 5]:
        def lambda_func(x):
            print(f'被filter调用了，x={x},n={i}')
            return x != i

        g2 = filter(lambda_func, g2)
        # 上一行等价于：g2 = filter(lambda x: x != i, g2)
    print(list(g2))


wrong_way()

# 错误原因解析
# lambda表达式引用了每轮循环的会变化的变量i
# 而且filter返回的是迭代器，它不会一次性计算出所有结果
# 而是保存当时的筛选条件，在next()调用时才根据保存的条件计算
# 这里的条件就是对应时期的lambda表达式以及它的变量和执行状态
# 前面说到i随着循环变化，lambda表达式直接引用i
# 迭代器又惰性计算，类似于引用了外部变化的量却未在变量变化之前调用的函数
# 所以当循环结束，迭代器记录的所有筛选方法的i都会变成最后一个i的值
# 而正确方法在使用i的函数外套再函数是为了把i作为参数绑定给每次的筛选方法
# 这样由于是不可变对象的赋值，所以外面的i变化不会影响到被绑定的参数
# 还有一个疑问待解决：g1 = (x for x in g1 if not_equal(i)(x))为什么不行
