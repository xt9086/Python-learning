#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
实现strStr()函数。
给你两个字符串haystack和needle，请你在haystack字符串中找出needle字符串出现的第一个位置（下标从0开始）。如果不存在，则返回-1 。

说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回0。

提示：
0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
"""


# 等复习了kmp等更高效的匹配算法再来优化


def str_str(haystack: str, needle: str) -> int:
    """方法1.调用字符串的find()方法"""
    return haystack.find(needle)


# def str_str(haystack: str, needle: str) -> int:
#     """方法2.暴力逐一比对，极端情况效率巨低，不推荐"""
#     # 若needle为空则返回0
#     if not needle:
#         return 0
#     # needle非空但haystack空则返回-1
#     elif not haystack:
#         return -1
#     len_hs = len(haystack)
#     len_nd = len(needle)
#     # 若needle比haystack长则返回-1
#     if len_nd > len_hs:
#         return -1
#     for i in range(len_hs):
#         # haystack的字符没遍历一次都要从该字符开始在内循环与needle的对应字符比对一轮
#         for j in range(len_nd):
#             # 只要不相等便推出本轮循环
#             if haystack[i + j] != needle[j]:
#                 break
#         # for...else语句仅当for中的break语句不执行才执行else内容
#         else:
#             return i
#         # haystack剩余字符长度小于needle则没必要再比较
#         if len_hs - i == len_nd:
#             break
#     return -1


if __name__ == '__main__':
    test_cases = [('hello', 'll', 2), ('like', '', 0), ('', '', 0), ('people', 'web', -1), ('hh', 'hhhh', -1)]
    for case in test_cases:
        r = str_str(case[0], case[1])
        print(case[2], r)
        assert case[2] == r
