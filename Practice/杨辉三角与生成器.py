#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""杨辉三角"""


# def yanghui_triangle():
#     """
#     自己想的方法，先算出每层除了首尾1的数
#     再和1拼接起来添加到杨辉三角列表
#     :return: None
#     """
#     floor_0 = [1]
#     # 第0层
#     yield floor_0
#     floor_1 = [1, 1]
#     # 第1层
#     yield floor_1
#     triangles = [floor_0, floor_1]
#     # 储存整个杨辉三角，每个元素对应每一层杨辉三角
#     n = 2
#     while True:
#         # 求第n层的杨辉三角列表
#         floor_n_center = []
#         for i in range(n - 1):
#             # 求第n层除了首尾1的数
#             floor_n_center.append(triangles[n - 1][i] + triangles[n - 1][i + 1])
#             # 第n层中间的第i个数等于第n-1层第i个数与第i+1个数的和
#         floor_n = floor_0 + floor_n_center + floor_0
#         # 将中间的数字列表与首尾的1拼接起来
#         triangles.append(floor_n)
#         # 将本层数字列表存入杨辉三角
#         n += 1
#         # 计算下一层
#         yield floor_n


# def yanghui_triangle():
#     """非常妙的方法
#     直接把上一层的数两两相加，得出下一行
#     通过补零使得两端的1可以由上一层的1加0得来
#     :return: None
#     """
#     floor = [1]
#     # 第一层
#     while True:
#         # 使用切片获得floor的副本是为了防止下面append(0)改变yield返回的值
#         yield floor[:]
#         # 在末端补零以便原来末端的1与现在的0相加生成下一层末端的1
#         floor.append(0)
#         # 将本层的数两两相加生成下一层的数列
#         # i=0时floor[1]+floor[-1]，正好相当于本层第一个元素1与最后补的0相加生成下一层的首个1
#         floor = [floor[i] + floor[i - 1] for i in range(len(floor))]

def yanghui_triangle():
    """最妙的方法
    同样是考虑直接把上一层的数两两相加，得出下一行
    但是该方法对首尾1的处理是通过在列表推导式里进行判断
    :return: None
    """
    n = 1
    # 首轮循环引用了floor元素的值，所以要提前赋值
    floor = []
    while True:
        # 杨辉三角第n层有n个元素，range(n)从0到n-1共n个元素
        # 遍历range(n)的元素若为0或者n-1，则列表推导式此轮为floor生成元素1
        # 相当于首尾都为1，其他元素由上一层相邻元素的和生成
        floor = [1 if m == 0 or m == n - 1 else floor[m-1]+floor[m] for m in range(n)]
        yield floor
        n += 1


if __name__ == '__main__':
    # k = 0
    # results = []
    # for t in yanghui_triangle():
    #     results.append(t)
    #     k = k + 1
    #     if k == 10:
    #         break
    #
    # for t in results:
    #     print(t)
    #
    # if results == [
    #     [1],
    #     [1, 1],
    #     [1, 2, 1],
    #     [1, 3, 3, 1],
    #     [1, 4, 6, 4, 1],
    #     [1, 5, 10, 10, 5, 1],
    #     [1, 6, 15, 20, 15, 6, 1],
    #     [1, 7, 21, 35, 35, 21, 7, 1],
    #     [1, 8, 28, 56, 70, 56, 28, 8, 1],
    #     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    # ]:
    #     print('测试通过!')
    # else:
    #     print('测试失败!')
    t = yanghui_triangle()
    print(next(t))
    print(next(t))
    print(next(t))
