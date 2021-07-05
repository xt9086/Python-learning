#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    """单链表结构定义"""

    def __init__(self, value=0, node=None):
        self.val = value
        self.next = node


############################################################


# def merge2lists(l1: ListNode, l2: ListNode) -> ListNode:
#     """方法1.自己想的
#     先分别遍历两个链表获取它们的值
#     再将它们的值存入一个列表进行排序
#     最后再根据排序好的值创建一个新链表
#     """
#     # 若两链表有一方为空，则返回另一链表，包括另一链表也为空
#     if not l1:
#         return l2
#     elif not l2:
#         return l1
#
#     def visit_node(list_node: ListNode):
#         """遍历访问链表的所有节点并将值存入列表返回"""
#         next_node = list_node
#         data = []
#         while True:
#             data.append(next_node.val)
#             # 若该节点的next为None，则表示没有后续节点，结束遍历
#             if not next_node.next:
#                 break
#             # 指向下一节点
#             next_node = next_node.next
#         return data
#
#     # 将两链表遍历的值组装成新的列表并排序
#     seq_data = sorted(visit_node(l1) + visit_node(l2))
#     # 创建首节点，并存在列表首位，利用列表记录节点间的顺序关系以及地址名称
#     nodes = [ListNode(seq_data[0])]
#     for i in range(1, len(seq_data)):
#         # 创建一个新的节点，添加到节点列表
#         # 也就是说通过列表名+下标指向该节点的地址
#         nodes.append(ListNode(seq_data[i]))
#         # 将前一节点的next指向当前节点
#         nodes[i - 1].next = nodes[i]
#     return nodes[0]


def merge2lists(l1: ListNode, l2: ListNode) -> ListNode:
    """方法2.辅助链表遍历
    使用辅助链表记录按两链表值大小顺序遍历的路径
    """
    # 记录p的路径
    p_head = ListNode(-1)
    # p.next指向当前遍历的节点
    p = p_head
    # 当两链表都不为空时，遍历两链表
    while l1 and l2:
        # 若l1的值小于等于l2的，则p的next指向l1节点
        if l1.val <= l2.val:
            p.next = l1
            # 移动至l1的下一个节点
            l1 = l1.next
        else:
            # 当l1的值>l2，则p的next指向l2节点
            p.next = l2
            # 移动至l2的下一节点
            l2 = l2.next
        # p也移动至next指向的下一节点
        p = p.next
    # 若两链表其一先遍历完，则将另一链表未遍历部分接到p.next
    p.next = l1 if l1 else l2
    # 由于开始p指向了p_head，所以之后p.next改变的同时p_head.next也随之改变了
    # 故p_head.next记录了p.next指向过的所有节点
    # 也就是说p_head.next就是原先两链表按值排序后合并成的新链表
    return p_head.next


# def merge2lists(l1: ListNode, l2: ListNode) -> ListNode:
#     """方法3.递归法
#     每次通过判断值大小得出当前节点，下一节点交给递归处理
#     """
#     # 当两链表有一为空则递归终止
#     if not l1:
#         return l2
#     elif not l2:
#         return l1
#     # 递归入口，无轮从l1还是l2开始，最终回溯时返回的链表都是原先两链表按值排序后合并成的新链表
#     if l1.val <= l2.val:
#         l1.next = merge2lists(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge2lists(l1, l2.next)
#         return l2


if __name__ == '__main__':
    # 测试
    def create_list(values: list):
        nodes = [ListNode(values[0])]
        for i in range(1, len(values)):
            nodes.append(ListNode(values[i]))
            nodes[i - 1].next = nodes[i]
        return nodes[0]


    def visit_node_test(list_node: ListNode):
        next_node = list_node
        data = []
        while True:
            data.append(next_node.val)
            if not next_node.next:
                break
            next_node = next_node.next
        return data


    case_values1 = [1, 2, 3, 4, 5]
    case_values2 = [0, 2, 4, 6, 8]
    case_seq = [0, 1, 2, 2, 3, 4, 4, 5, 6, 8]
    list1 = create_list(case_values1)
    list2 = create_list(case_values2)

    new_list = visit_node_test(merge2lists(list1, list2))
    print(case_seq, new_list)
    assert case_seq == new_list
    test_cases = [
        ([], list2, list2),
        (list1, [], list1),
        ([], [], [])
    ]
    for n in test_cases:
        r = merge2lists(n[0], n[1])
        print(n, r)
        assert n[2] == r
