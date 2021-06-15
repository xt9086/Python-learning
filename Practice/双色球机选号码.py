#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""双色球开奖"""

import random
import time


def lottery_draw():
    """ 双色球彩票号码随机生成 """
    red_ball = list(range(1, 34))
    num = []
    # for i in range(1,7):
    #     temp = random.choice(red_ball)
    #     num.append(temp)
    #     red_ball.remove(temp)
    p = 1
    while p < 7:
        p = p + 1
        temp = random.choice(red_ball)
        num.append(temp)
        red_ball.remove(temp)  # 删除不计已摇出的红球
    num.sort()  # 将红球号码从小到大排序
    # 生成蓝球号码
    num.append(random.randint(1, 16))
    return num


if __name__ == "__main__":

    tag = input('输入y获取彩票开奖结果：')

    while tag == 'y':
        print('正在开奖...')
        lottery_num = lottery_draw()
        i = 1
        for n in lottery_num[0:6]:
            # print('第',i,'个红球号码是：',n)
            # print('第'+str(i)+'个红球号码是：'+str(n))
            # print('第%d个红球号码是：%d' %(i,n))
            # print('第{0}个红球号码是:{1}'.format(i,n))
            print(f'第{i}个红球号码是：{n}')
            i = i + 1
            time.sleep(1)
        print('最后1个蓝球号码为：', lottery_num[6])
        print('本期开奖的最终结果为：')
        k = 0
        for m in lottery_num:
            k = k + 1
            if k == 6:
                print(m, end=' + ')
            else:
                print(m, end=' ')
        tag = input('\n是否继续开奖(y/n)：')
    print('祝您好运！')
