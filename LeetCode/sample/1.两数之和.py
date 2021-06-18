#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给定一个整数数组 nums 和一个整数目标值 target,
请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""


# 方法1.暴力枚举
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# 方法2.假设n+m=target,从后面找满足假设的m
# def two_sum(nums, target):
#     for i, n in enumerate(nums):
#         # 遍历列表，每次假设当前元素加另一个元素等于target
#         # 若假设成立则另一个元素必然在后续列表中
#         m = target - n
#         if m in nums[i + 1:]:
#             # 另一个元素的下标要从n元素的下一个开始找
#             return [i, nums.index(m, i + 1)]


# 方法3.哈希（散列）表,性能最高
def two_sum(nums, target):
    hash_dict = {}
    # 假设m+n=target, 从前面字典存的键找满足假设的n
    for i, n in enumerate(nums):
        m = target - n
        if m in hash_dict:
            return [hash_dict[m], i]
        # 插入放在判断之后，不然刚插入的键永远满足判断的条件
        hash_dict[n] = i


if __name__ == '__main__':
    test_case1 = ([3, 2, 4], 6)
    result_1 = two_sum(*test_case1)
    print(result_1)
    assert result_1 == [1, 2]

    test_case2 = ([2, 2], 4)
    result_2 = two_sum(*test_case2)
    print(result_2)
    assert result_2 == [0, 1]
