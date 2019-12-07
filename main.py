#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick


"""
卡片收集问题: https://blog.csdn.net/wenrr89/article/details/54688469
python实现第二类Stirling数: https://blog.csdn.net/LuYi_WeiLin/article/details/85390096
计算排列组合数-python: https://blog.csdn.net/weixin_41481113/article/details/82845269
如果一个男/女生说，他/她集齐了十二个星座的前任: https://www.zhihu.com/question/38331955


"""

import math
from stirling2_lookup_table import Stirling2LookupTable
from coupon_collector_solver import CouponCollectorSolver

def stirling2(n: int, m: int):
    if m > n or m == 0:
        return 0
    if n == m:
        return 1
    if m == 1:
        return 1
    return stirling2(n - 1, m - 1) + stirling2(n - 1, m) * m



def cdf(n: int, m: int):
    return math.factorial(m) * stirling2(n, m) / pow(m, n)

def pdf(n: int, m: int):
    return math.factorial(m) * stirling2(n - 1, m - 1) / pow(m, n)

# print(stirling2(10, 9))
stirling2_table = Stirling2LookupTable(9, 9)
#print(stirling2_table)
solver = CouponCollectorSolver(0)

for i in range(0, 10):
    print(solver.pdf(i))


def cdf(number_of_cards: int):
    pass