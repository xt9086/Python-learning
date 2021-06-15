#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""字典练习"""
students = [
    {'name': 'a', 'grade': 88, 'gender': 'male'},
    {'name': 'b', 'grade': 61, 'gender': 'unknown'},
    {'name': 'c', 'grade': 99, 'gender': 'unknown'},
    {'name': 'd', 'grade': 75, 'gender': 'unknown'},
    {'name': 'e', 'grade': 99, 'gender': 'female'},
]
students_copy = students[:]
#   1.删除性别未知的学生

# 错误示范：
# 注意删除元素时，元素总个数也会减少
# 所以下面for循环遍历途中会因元素被删除而导致索引前移，继而漏删数据
# for std in students:
#     if std['gender'] == 'unknown':
#         students.remove(std)
# print(students)

# 方法一
# for std in students_copy[:]:
#     # 遍历的是std，删除的是std的切片，所以不会影响
#     if std['gender'] == 'unknown':
#         students_copy.remove(std)
# print(students_copy)

# 方法二
# std_temp = []
# for std in students_copy:
#     # 把不是性别位置的学生存到另一个列表再赋值给原列表
#     if std['gender'] != 'unknown':
#         std_temp.append(std)
# students_copy = std_temp
# print(students_copy)

# 方法三
# 原理同方法二，只是使用了列表推导式
# students_copy = [std for std in students_copy if std['gender'] != 'unknown']
# print(students_copy)

# 方法四
# rang(m,n,k)表示 m,m+k,m+2k,...,n-(n-m)%k 的序列
# 所以下面生成的是个从大到小逆序的一个序列
# 也可以通过reversed(range(len(students_copy) - 1))生成逆序列
# 按着逆序的索引循环，不会使索引发生位移
for i in range(len(students_copy) - 1, -1, -1):
    # for i in reversed(range(len(students_copy) - 1)):
    if students_copy[i]['gender'] == 'unknown':
        students_copy.remove(students_copy[i])
print(students_copy)

# 方法五
# i = 0
# while i < len(students_copy):
#     if students_copy[i]['gender'] == 'unknown':
#         students_copy.remove(students_copy[i])
#         # 删除一个元素后，下一个要访问的元素索引前移了一个单位
#         # 所以要循环的索引i也要减1才对
#         i -= 1
#     i += 1
# print(students_copy)


#   2.将列表按学生成绩从大到小排序
for i in range(len(students) - 1):
    tag = True
    for j in range(len(students) - 1 - i):
        if students[j]['grade'] < students[j + 1]['grade']:
            students[j], students[j + 1] = students[j + 1], students[j]
            tag = False
    if tag:
        break
print(students)
