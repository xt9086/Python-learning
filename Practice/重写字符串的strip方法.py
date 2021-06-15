#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""从头实现字符串的strip方法"""


def my_strip(s, sep=None):
    """
    基本实现str对象内置的strip方法
    默认参数sep缺省则默认删除首尾空白字符
    否则删除sep里保护的字符
    :param s: 原字符串
    :param sep: 要删除的字符，默认为None
    :return: 原字符串已删除首尾指定字符的副本
    """
    s_copy = s[:]
    # 创建原字符串的副本
    filter_str = ' \n\r\t\v\f'
    # 常见的空白字符
    # ' '空格，'\n'换行，'\r'回车，'\t'水平制表符，'\v'垂直制表符，'\f'翻页
    # 另外string模块定义了变量whitespace=' \t\n\r\v\f'，可以引入模块直接使用
    if sep is not None:
        # 若sep是None则默认删除首尾空白字符
        # 否则删除sep里包含的字符
        filter_str = sep
    while s_copy[:1] != '' and s_copy[:1] in filter_str:
        # 注意空字符串''in任何字符串都为True，要进行判断不然会死循环
        # 若首字符是filter_str字符串里字符的任意一个
        # 则排除该字符，切片保留后续字符
        s_copy = s_copy[1:]
    while s_copy[-1:] != '' and s_copy[-1:] in filter_str:
        # 清除尾端指定字符
        s_copy = s_copy[:-1]
    return s_copy


if __name__ == '__main__':
    # 测试
    s1 = '  I like you   \n\t'
    s2 = '++-hello+-'
    print(s1)
    print(s1.strip())
    print(my_strip(s1))
    print(my_strip(s2, '+-'))
