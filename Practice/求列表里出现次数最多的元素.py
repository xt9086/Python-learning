#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""求列表里出现次数最多的元素"""

# L = ' '.join(input('请输入一段字符：')).split()
L = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2]
# L = [2, 3, 9, 2, 2, 5, 1, 1, 3, 1, 8, 10]
print(L)

#   1.自己第一次想的方法，比较麻烦不推荐
L_temp = L[:]
L1 = []
result = []
# 两层for循环求出列表各个元素出现的次数
for i in range(len(L) - 1):
    # 设每个元素初始出现次数为1
    count = 1
    # 内循环每次将取得的元素与后面的元素进行比较
    # j为要与取得元素比较的下一个元素的索引，故从1开始取
    for j in range(1, len(L_temp)):
        # 每轮参与比较的元素都会被删除，
        # 若相等则出现次数+1，并删除右侧那个元素，避免外循环重复选择一样的元素
        # 若不相等则跳过此元素与下一个元素继续比较
        # 由于相等时，删除元素会导致列表元素变少，为了不出现下标索引超出范围
        # 故j减去上一轮删除的元素个数(count-1)
        if L_temp[0] == L_temp[j - count + 1]:
            count += 1
            # 此处不能用remove()，因为它是删除从左到右第一个与参数相符的元素
            # count增加了1，下面减count要比原来多减1，故再加1
            L_temp.pop(j - count + 2)
    # 每轮内层循环后把统计的元素与次数存入列表
    L1.extend([L_temp[0], count])
    # 将此轮被选中已经比较过的元素删除
    L_temp.pop(0)
    # 若列表为空，说明所有元素出现次数已经统计完毕，退出循环
    if not L_temp:
        break

print('各元素出现次数', L1)
# 设初始最大数为L1[1]
max_num = L1[1]
print(L1[3::2])
# 元素出现次数存在L1的奇数索引对应元素下
# 将其次数对应元素切片并遍历求最大值
for value in L1[3::2]:
    if value > max_num:
        # 若有元素比之前的最大值大，则将元素值赋给它
        # 保证max_num最终是最大值
        max_num = value

print(max_num)
print(L1[1::2])

# 求最大次数对应的元素
for k in range(len(L1)):
    # 若索引为偶数且下一个值为最大次数
    # 则该索引对应元素便是出现次数最多的元素之一
    if k % 2 == 0 and L1[k + 1] == max_num:
        result.append(L1[k])

#   2.使用字典存结果，比较高效
# from 获取列表中每个元素出现的次数 import count_elements
#
# # 导入写好的模块中求列表里每个元素出现的次数的方法
# # 将统计结果存入字典
# d_count = count_elements(L)
# print(d_count)
# # 求出出现次数的最大值
# max_num = max(d_count.values())
# print(max_num)
# result = []
# for k, v in d_count.items():
#     # 遍历字典找出值为max_num的键
#     if v == max_num:
#         result.append(k)


print(result)
print("出现次数最多的元素为：", end='')
for r in result:
    print(r, end=',')
print("出现了%d次" % max_num)
