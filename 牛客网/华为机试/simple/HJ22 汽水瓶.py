#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
描述
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？
”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。
然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？

输入描述：
输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=100），
表示小张手上的空汽水瓶数。n=0表示输入结束，你的程序不应当处理这一行。

输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

示例1
输入：
3
10
81
0
输出：
1
5
40

来源：https://www.nowcoder.com/practice/fe298c55694f4ed39e256170ff2c205f?tpId=37&&tqId=21245&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking
"""


# def calc(num):
#     """方法1.递归计算可兑换的饮料数"""
#     if num < 2:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return num // 3 + calc(num // 3 + num % 3)


def calc(num):
    """方法2
    实质上每次用两个空瓶就可以借一瓶饮料，随后原来的两个瓶子加上本次喝完的第三个瓶子又都会还回去。
    所以只用计算n个空瓶整除以2的整数结果，即n//2。
    """
    return num // 2


if __name__ == '__main__':
    # 输入
    test = []
    n = 1
    while n:
        n = int(input())
        test.append(n)

    # 输出
    for case in test:
        if not case:
            break
        print(calc(case))
