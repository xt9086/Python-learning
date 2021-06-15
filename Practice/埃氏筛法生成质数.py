#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
"""


def odd_generator():
    """生成无限个奇数的生成器函数"""
    n = 1
    while True:
        n += 2
        yield n


# def not_divisible(n):
#     """
#     将序列的上一个值n绑定，防止被后来的n覆盖
#     返回匿名函数判断x是否为n的倍数
#     x在filter调用匿名函数时由sieve_seq传入
#     """
#     return lambda x: x % n > 0

# 下面函数等同于上面的

def not_divisible(n):
    def lam(x):
        print(f'被filter调用x={x},n={n}')
        return x % n > 0

    return lam


def primes_generator():
    # 唯一个偶数质数2
    yield 2
    # 初始生成器序列
    sieve_seq = odd_generator()
    while True:
        # 获取当前生成器序列第一个值
        n = next(sieve_seq)
        yield n
        # 使用filter筛选掉非质数
        sieve_seq = filter(not_divisible(n), sieve_seq)
        # sieve_seq = (x for x in sieve_seq if (lambda x, m=n: x % m > 0)(x))
        # 对于上面这句我开始觉得为什么要多此一举把匿名函数套个函数壳传入上个n
        # 而不直接这样写sieve_seq=filter(lambda x: x % n > 0, sieve_seq)
        # 但是我改成上面的代码后运行发现输出的序列完全未被筛选，为什么呢？
        # 因为sieve_seq是无限生成奇数的生成器，filter不可能瞬间把无穷个元素都筛选一遍
        # filter只会返回记录本次筛选的方法的迭代器，每次被next调用时再筛选计算直到取到值停止
        # 所以每次next取filter返回的迭代器的值时，不仅要被本轮的n筛选还要接受之前的所有n筛选
        # 因为之前的n筛选方法被记录了，它不是立即作用在整个序列，而是每轮调用作用一次
        # 前面扯远了，现在回到开始的问题，为什么lambda表达式要用函数包裹
        # 因为匿名函数与filter形成了闭包，而且是未通过传参引用了外部随着循环变化的n
        # filter返回的又是迭代器，它只保存了计算的方法，没有立即计算值
        # 类似引用了外部循环变量却未在变量变化之前调用的函数
        # 所以当循环结束，迭代器记录的所有筛选方法的n都会变成最后一个n的值
        # 在lambda表达式外套函数是为了把n作为参数绑定给每次的筛选方法
        # 还有一种绑定方法是这样写：sieve_seq = filter(lambda x, m=n: x % m > 0, sieve_seq)


if __name__ == '__main__':
    primes = []
    for i in primes_generator():
        if i > 20:
            break
        print(i)
        primes.append(i)
    print(primes)
    # g = primes_generator()
    # print(next(g))
    # print(next(g))
    # print(next(g))
