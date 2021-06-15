#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""封装程序运行时间函数的模块"""
import time


def calc_run_time(func):
    """
    计算十次程序运行时间取均值
    :param func: 待计算的函数
    :return: 函数十次运行时间的均值(单位:纳秒)
    """
    total_time = 0
    for i in range(10):
        stat_time = time.perf_counter_ns()
        func()
        end_time = time.perf_counter_ns()
        total_time += end_time - stat_time
    return total_time / 10


if __name__ == "__main__":
    def test_func():
        # sum_i = 0
        # for i in range(10000000):
        #     sum_i += i
        time.sleep(1)


    print(calc_run_time(test_func)*10**-9, '秒')
