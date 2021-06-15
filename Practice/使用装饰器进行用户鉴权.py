#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""使用装饰器进行用户鉴权"""

user_permissions = 7  # 111
read_permission = 4  # 100
write_permission = 2  # 010
delete_permission = 1  # 001


# 二进制的每一位可以表示一种权限，1为允许，0为禁止
# 具体一个权限可以将表示权限的二进制数对应位置1，其余位置0
# 一个表示用户权限的数字可以是多个权限的组合
# 比如7也就是二进制的111，三位都是1表示有三种权限的许可
# 将相同位数的用户权限数与对应功能权限数按位相与
# 若结果不为0，则代表该用户拥有该权限的许可
# n位2进制数可以表示n种权限，这n种权限有2**n种组合（包括所有权限都为0，即空集）


def check_permission(pm_user, pm_action):
    # 外层函数用来接收附加参数
    def decorator(func):
        # 中间函数用来接收被装饰的函数
        def wrapper():
            # 最内层函数使用上述参数为被装饰函数添加功能并调用它
            if pm_user & pm_action != 0:
                func()
            else:
                print('对不起，您没有此权限！')

        return wrapper

    return decorator


@check_permission(user_permissions, read_permission)
def user_read():
    print('正在读取...')


@check_permission(user_permissions, write_permission)
def user_write():
    print('正在写入...')


@check_permission(user_permissions, delete_permission)
def user_delete():
    print('正在删除...')


if __name__ == '__main__':
    user_read()
    user_write()
    user_delete()
# 装饰器执行顺序举例说明
# 首先执行check_permission(user_permissions, delete_permission)
# 得到返回值decorator，再使得user_read=decorator(user_read)
# 得到返回值wrapper,执行user_read()相当于执行wrapper()
# wrapper()执行时判断通过后又调用了func，即原来的user_read
