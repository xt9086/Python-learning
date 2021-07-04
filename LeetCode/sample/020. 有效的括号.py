#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

我的理解：
1.左右括号必须成对出现，错误示范：(((
2.右括号前面必须有一左括号与之配对，错误示范：)(
3.不同类型的括号不能交叉嵌套，错误示范：[{]}

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
"""


# def is_valid(s: str) -> bool:
#     """1.原版，先剔除字符为奇数个以及同类左右括号数不相等的情况，再使用栈"""
#     if len(s) % 2 != 0:
#         return False
#     elif s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
#         return False
#     brackets = ['(', ')', '[', ']', '{', '}']
#     s_stack = []
#     for e in s:
#         if e in ['(', '[', '{']:
#             s_stack.append(e)
#         else:
#             # 通过index方法再brackets里查找右括号e的下标，其下标减一对应的是同类左括号
#             if not s_stack or brackets[brackets.index(e) - 1] != s_stack[-1]:
#                 return False
#             s_stack.pop()
#     return True


def is_valid(s: str) -> bool:
    """2.基于1进行优化
    使用count()方法计数效率要比最后判断栈空慢
    优化brackets以及通过右括号找左括号的方法
    """
    if len(s) % 2 != 0:
        return False
    # 记录了左右括号的对应关系，便于通过右括号找出对应的左括号
    brackets = {')': '(', ']': '[', '}': '{'}
    # 初始化空栈
    s_stack = []
    for e in s:
        # in访问字典实际是默认访问字典的所有键，也就是三种右括号
        # 若e是右括号
        if e in brackets:
            # 此时栈空表示前面没有能与当前右括号配对的左括号，返回False
            # 此时右括号对应的左括号若与栈顶的左括号不一样
            # 则说明有不同类的括号交叉嵌套于此，返回False
            if not s_stack or brackets[e] != s_stack[-1]:
                return False
            # 配对成功并把已匹配的栈顶左括号弹出
            s_stack.pop()
        else:
            # 若e是左括号便直接进栈
            s_stack.append(e)
    # 若字符串遍历完了栈里还有未能配对的括号则返回False
    # if s_stack:
    #     return False
    # return True
    # 上述代码可简写为下面这句：
    return not s_stack


if __name__ == '__main__':
    test_cases = {
        '[[]': False,
        '((()': False,
        ')([]': False,
        '[}{]': False,
        '{[(])}': False,
        '{[()[]{}]}': True
    }
    for case in test_cases:
        r = is_valid(case)
        print(case, r)
        assert test_cases[case] == r
