#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""获取列表中每个元素出现的次数并与元素值成对存入字典"""

import time

import collections

# data_list = ' '.join('''3.14159265358979我满意什么？评论区弹幕确实很多人不理性，但我视频里是号召大家给他判私刑了吗，
# 你竟然会认为我是在用舆论判刑？我整个视频都是理性陈述事实，也没因为愤怒就说有内幕收钱了没搞对立阴谋论。
# 我来给你捋一下，事情最开始温州交警自媒体号发了陈袭警却只被拘留的视频，视频中并没有说明是辅警，更没有解释辅警不适用于袭警罪。
# 所以网友们看到这视频发现打警察竟然不用判袭警罪拘留几天就出来了，于是就会产生有黑幕的猜疑。
# 而温州公安面对无数网友在其各平台账号的质疑声选择视而不见，甚至偷偷删掉原视频。要是作为当时的网友你会怎么想？
# 于是就有了包括我在内的很多网友去信访举报投诉，每天在温州交警官方号下提此事件。这样，才有当地公安局才给我个人如视频中所见的回复。
# 当地公安的的回复很合理，我也没在视频里说他瞎扯啊。但是我就不能提出自己的看法了吗，而且我的观点并不是凭我主观好恶提出的。
# 妨害公务罪的主体是依法执行职务的国家工作人员，而辅警算不算是有争议的，以及我在网上找到了法院公布的攻击单独执法辅警被判妨害公务的案例。
# 所以我为什么不能提出疑问呢？合着我就该股掌说判的好，大人英明？
# 4月14的事情如果当地公安能及时回应给大家解释，会过去一个月了还闹得群情激愤吗？''').split()


# data_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2]
# data_list = [2, 3, 9, 2, 2, 5, 1, 1, 3, 1]

#   方法一
# def count_elements(dt_list):
#     dt_dict = {}
#     for i in range(len(dt_list)):
#         if i >= len(dt_list):
#             break
#         count = 1
#         for j in range(i + 1, len(dt_list)):
#             if dt_list[i] == dt_list[j - count + 1]:
#                 count += 1
#                 dt_list.pop(j - count + 2)
#         dt_dict[dt_list[i]] = count
#     return dt_dict
# t_end - t_start = 5829300 速度排名：5

#   方法一的优化
# def count_elements(dt_list):
#     dt_copy = dt_list[:]
#     dt_dict = {}
#     for i in range(len(dt_list) - 1):
#         count = 1
#         for j in range(1, len(dt_copy)):
#             if dt_copy[0] == dt_copy[j - count + 1]:
#                 count += 1
#                 dt_copy.pop(j - count + 2)
#         dt_dict[dt_copy[0]] = count
#         dt_copy.pop(0)
#         if not dt_copy:
#             break
#     return dt_dict


# t_end - t_start = 4984400 速度排名：4


#   方法二
# def count_elements(dt_list):
#     dt_dict = {}
#     for i in dt_list:
#         if i not in dt_dict:
#             dt_dict[i] = dt_list.count(i)
#     return dt_dict
# t_end - t_start = 2144100 速度排名：3


#   方法三
def count_elements(dt_list):
    dt_dict = {}
    for i in dt_list:
        # 遍历列表里的元素
        # 若字典里的键没有这个元素，那将这个元素作为键，出现的次数1作为值存入字典
        # 若字典里的键已有了这个元素，那将它的值+1
        # 最后返回字典
        if i not in dt_dict:
            dt_dict[i] = 1
        else:
            dt_dict[i] += 1
    return dt_dict
# t_end - t_start = 166500 速度排名：1


#   方法四
# def count_elements(dt_list):
#     return dict(collections.Counter(dt_list))
# t_end - t_start = 182100 速度排名：2


# if __name__ == "__main__":
#     t_start = time.perf_counter_ns()
#     print(count_elements(data_list))
#     t_end = time.perf_counter_ns()
#     print(t_start)
#     print(t_end)
#     print(t_end - t_start)
