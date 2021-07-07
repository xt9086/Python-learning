#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给你一个有序数组 nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ，并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


# def remove_duplicates(nums) -> int:
#     """方法1.边比较边删除重复值
#     但是该方法在leetcode提交执行的时间高达1100ms
#     """
#     # 若数组空返回0，无需其他操作
#     if not nums:
#         return 0
#     i = 1
#     # 从第二个元素开始遍历
#     while i < len(nums):
#         # 若比和前一个元素相同，则删除该重复值
#         if nums[i] == nums[i - 1]:
#             nums.pop(i)
#             # 由于删除了一个值后面元素的索引前移，不需要再+1
#         else:
#             # 未删除元素，则需+1才能访问下一个元素
#             i += 1
#     # 循环退出时的 i 值便是数组的长度
#     return i


def remove_duplicates(nums) -> int:
    """方法2.赋值法（快慢双指针法）
    将不重复的元素通过赋值移到数组前面
    使数组前一部分是不重复的值，后一部分是与前面值重复的
    """
    if not nums:
        return 0
    # 索引 i 用来从1开始遍历整个原数组
    # 索引 k 从1开始自增，用于指向不重复元素要赋值的位置
    i = k = 1
    n = len(nums)
    while i < n:
        # 若元素与前一个元素不重复，则将该元素的值赋给nums[k]
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
        i += 1
    # leetcode提交时只要保证修改后的数组前k个值是不重复的就能通过
    # 要真的删除重复值可以加上以下代码：
    # for j in range(n - k):
    #     nums.pop()
    return k


if __name__ == '__main__':
    nm = sorted(list(range(10)) + list(range(20)) + list(range(30)))
    print(remove_duplicates(nm))
    print(nm)
