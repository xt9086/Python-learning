#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""重新实现range类的功能"""


class MyRange(object):
    """基本实现内置range的所有功能"""
    def __init__(self, *args: int):  # 提示建议为整型
        """初始化进行参数检查及绑定"""
        if len(args) == 0:
            # 至少要传一个参数
            raise TypeError('MyRange expected 1 arguments, got 0')
        elif len(args) > 3:
            # 最多只允许传3个参数
            raise TypeError(f'MyRange expected at most 3 arguments, got {len(args)}')
        for arg in args:
            # 若参数不是整型，则抛出类型错误
            if not isinstance(arg, int):
                raise TypeError(type(arg).__name__ + ' object cannot be interpreted as an integer')
        self.start = 0
        self.step = 1
        self.index = 0
        if len(args) == 1:
            # 若只有一个参数，则它就是数列末项的边界，且无法取到
            self.stop = args[0]
        elif len(args) >= 2:
            # 两个参数以上，则参数0是首项，参数1是末项的边界
            self.start = args[0]
            self.stop = args[1]
        if len(args) == 3:
            # 若有三个参数，则参数2为步长
            if args[2] == 0:
                # 步长不能为0
                raise ValueError('MyRange() arg 3 must not be zero')
            self.step = args[2]

    def __iter__(self):
        """重写__iter__方法，返回自身的迭代器对象"""
        return self

    def __next__(self):
        """重写__next__方法，每次调用返回递推得出的通项"""
        if self.step > 0 and self.start < self.stop:
            # 若step为正，通项公式为r[i]=start+step*i，其中i>=0且r[i]<stop
            self.start += self.step
            return self.start - self.step
        elif self.step < 0 and self.start > self.stop:
            # 若step为负，通项公式仍为r[i]=start+step*i，但其中i>=0且r[i]>stop
            self.start += self.step
            return self.start - self.step
        else:
            raise StopIteration

    # def __next__(self):
    #     """重写__next__方法,每次调用返回通项公式计算出的项"""
    #     term = self.start + self.index * self.step
    #     # 首项为start、公差为step的等差数列通项公式
    #     # 共n项，首项下标为0，第n项下标为n-1
    #     if self.step > 0 and term < self.stop:
    #         self.index += 1
    #         return term
    #     elif self.step < 0 and term > self.stop:
    #         # 步长也就是公差为负时，每项的值逐级递减
    #         # 前一项大于后一项才有意义，stop是最后最小一项，且不能取到
    #         self.index += 1
    #         return term
    #     else:
    #         # 抛出StopIteration异常可以停止产生下一项
    #         raise StopIteration


if __name__ == '__main__':
    if list(MyRange(10)) != list(range(10)):
        print('测试失败')
    elif list(MyRange(1, 10)) != list(range(1, 10)):
        print('测试失败')
    elif list(MyRange(2, 20, 3)) != list(range(2, 20, 3)):
        print('测试失败')
    elif list(MyRange(10, 20, 4)) != list(range(10, 20, 4)):
        print('测试失败')
    elif list(MyRange(10, -1, -2)) != list(range(10, -1, -2)):
        print('测试失败')
    else:
        print('测试成功！！！')

    result = []
    for i in MyRange(10, 21, 3):
        result.append(i)
    print(result)
