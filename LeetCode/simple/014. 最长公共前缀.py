#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串。
提示：
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix/
"""


# def longest_common_prefix(strs) -> str:
#     """方法1.横向查找"""
#     if not strs:
#         return ''
#     longest_prefix = strs[0]
#     # 初始假定最长前缀，随着往后遍历的条件限制进行修正
#     for i in range(len(strs) - 1):
#         # 临时保存每轮内循环获取的公共前缀
#         prefix = ''
#         # 内循环将上一轮的前缀与strs里下一个字符串每个字母依次比对
#         # 只要匹配不上就退出本轮内循环
#         for j in range(len(longest_prefix)):
#             if j >= len(strs[i + 1]) or longest_prefix[j] != strs[i + 1][j]:
#                 break
#             else:
#                 prefix += longest_prefix[j]
#         # 若prefix为空，则表示没有公共前缀
#         if not prefix:
#             return ''
#         longest_prefix = prefix
#     return longest_prefix


def longest_common_prefix(strs) -> str:
    """方法2.纵向查找"""
    prefix = ''
    # 若strs为或者作为参考值的strs[0]为空字符，则返回空字符
    # 注意not strs必须要放在not strs[0]前面判断，不然会下标越界
    if not strs or not strs[0]:
        return ''
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                return prefix
        prefix += strs[0][i]
    return prefix


if __name__ == '__main__':
    test_cases = \
        [
            (["flower", "flow", "flight"], 'fl'),
            (["dog", "race", "car"], ''),
            (['a'], 'a'),
            ([''], ''),
            (['a', '', 'c'], ''),
            ([], '')
        ]
    for k in test_cases:
        r = longest_common_prefix(k[0])
        print(k[0], r)
        assert k[1] == r
