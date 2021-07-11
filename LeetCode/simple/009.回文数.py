#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
"""


# def is_palindrome(n):
#     """方法1：从两端开始逐一比对"""
#     s = str(n)
#     for i in range(len(s)):
#         if s[i] != s[len(s) - i - 1]:
#             return False
#     return True


def is_palindrome(n):
    """方法2:若与自己的逆序切片相等则是回文数"""
    s = str(n)
    return s == s[::-1]

# def is_palindrome(n):
#     """方法3：使用reversed()函数"""
#     s = str(n)
#     # reversed(s)返回的是迭代器，通过list函数获取序列
#     # 同时字符串s也要转为list类型
#     return list(s) == list(reversed(s))

# def is_palindrome(n):
#     """不转字符串，利用余数"""
#     if n < 0:
#         return False
#     nums = []
#     while True:
#         nums.append(n % 10)
#         n = n // 10
#         if not n:
#             break
#     return nums == nums[::-1]


if __name__ == '__main__':
    num = 12321
    if is_palindrome(num):
        print("是")
    else:
        print("不是")
