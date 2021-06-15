#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""提取字符串丽的所有数，包括负数、浮点数"""

import re
# -3.14dd-1.73da-2.dasd4.dasd100sss99.888jj.66
mix = input('输入字符串:')
nums = re.finditer(r"([-]?)(0|[1-9]\d*)+(\.\d+)?", mix)
value_list = []
for n in nums:
    value_list.append(n)
result = 0
for i in value_list:
    result += float(i.group())
print(result)
