#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#1. 编写程序，生成一个包含20个随机整数
# 的列表，然后对其中偶数下标（下标即列
# 表元素的索引）的元素进行降序排列，奇
# 数下标的元素不变。（提示：使用切片。）
# import random
# x=[random.randint(0,100) for i in range(20)]
# print(x)
# y=x[::2]
# y.sort()
# y.reverse()
# x[::2]=y
# print(x)

# import  random
# x=[random.randint(0,100)for i in range(20)]
# print(x)
# y=x[::2]
# y.sort()
# y.reverse()
# x[::2]=y
# print(x)

# 2.随机生成一个包含1000个字母的字符串，然后
# 统计该字符串中每个字母的数量，并输出结果
# （要求结果以字典方式存储）
# from string import ascii_letters,digits
# from collections import Counter
# from random import choice
# ss = ascii_letters+digits
# L=[choice(ss)for i in range(1000)]
# c=Counter(L)
# for k,v in c.most_common():
#     print(k,v)

from string import  ascii_letters,digits
from  collections import  Counter
from  random import choice
ss=ascii_letters+digits
L=[choice(ss)for i in range(1000)]
c=Counter(L)
for k,v in c.most_common():
    print(k,v)

# import random
# x=[random.randint(0,100)for i in range(20)]
# print(x)
# y=x[::2]
# y.sort()
# y.reverse()
# x[::2]=y
# print(x)

import random
x=[random.randint(0,100)for i in range(20)]
print(x)
y=x[::2]
y.sort()
y.reverse()
x[::2]=y
print(x)