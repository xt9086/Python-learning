#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""验证是否为回文数"""


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


if __name__ == '__main__':
    num = 123
    if is_palindrome(num):
        print("是")
    else:
        print("不是")
