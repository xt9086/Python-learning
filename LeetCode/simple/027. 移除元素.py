#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给你一个数组 nums 一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
"""


# def remove_element(nums: list, val: int) -> int:
#     """方法1.边比较边删除等于val的值"""
#     if not nums:
#         return 0
#     # 遍历nums的副本，避免受到元素被删除后索引前移的影响
#     for n in nums[:]:
#         if val == n:
#             nums.remove(n)
#     return len(nums)


def remove_element(nums: list, val: int) -> int:
    """方法2.双指针法"""
    if not nums:
        return 0
    i = k = 0
    n = len(nums)
    while i < n:
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        i += 1
    return k


if __name__ == '__main__':
    test_case = [3, 1, 4, 1, 5, 9, 2, 6]
    order_case = sorted([3, 4, 5, 9, 2, 6])
    k = remove_element(test_case, 1)
    print(k, test_case)
    assert order_case == sorted(test_case[:k])
    assert k == len(order_case)
