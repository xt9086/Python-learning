#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""汉诺塔问题"""


# 递归与分治法
def move(n, a, b, c):
    """
    打印解决n块盘子汉诺塔问题的步骤
    形参a,b,c的位置对应起始柱，中转柱，目标柱
    在调用中形参对应的实参值会变，意味着a,b,c扮演的角色时变化的
    :param n: 初始A柱子盘子块数
    :param a: 起始柱
    :param b: 中转柱
    :param c: 目标柱
    :return: None
    """
    if n == 1:
        # n=1时直接从A移到C即可
        print(a, '-->', c)
    else:
        # 把A柱的盘子分两份，上面n-1块从C中转移到B
        move(n - 1, a, c, b)
        # A柱只剩下最底下编号为n的盘子时，将它一步移到C柱
        print(a, '-->', c)
        # 接下来只用把剩下的n-1块盘中从B中转A再移到C
        move(n - 1, b, a, c)


if __name__ == '__main__':
    # test
    print(move(3, 'A', 'B', 'C'))
