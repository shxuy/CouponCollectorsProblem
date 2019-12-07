#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick


"""
卡片收集问题: https://blog.csdn.net/wenrr89/article/details/54688469
python实现第二类Stirling数: https://blog.csdn.net/LuYi_WeiLin/article/details/85390096
计算排列组合数-python: https://blog.csdn.net/weixin_41481113/article/details/82845269
如果一个男/女生说，他/她集齐了十二个星座的前任: https://www.zhihu.com/question/38331955
赠券问题的均值和方差：https://brilliant.org/wiki/coupon-collector-problem/
           n
Var[X]=n^2 ∑ (1/k^2) - n * Hn
          k=1

"""

import numpy as np

def stirling2(n: int, m: int):
    if m > n or m == 0:
        return 0
    if n == m:
        return 1
    if m == 1:
        return 1
    return stirling2(n - 1, m - 1) + stirling2(n - 1, m) * m

"""
for i in range(10):
    s = ""
    for j in range(10):
        s += str(stirling2(i, j)) + "\t"
    #print(s)
"""


def factorial(n: int):
    """
    高精度阶乘
    scipy.special里的factorial返回一个浮点数，容易导致计算结果不精准，所以这里重复造轮子
    :param n: 自然数
    :return: n!
    """
    if not isinstance(n, int) or n < 0:
        raise Exception('阶乘的参数应为正整数')
    if n == 0 or n == 1:
        return 1
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def cdf(n: int, m: int):
    return factorial(m) * stirling2(n, m) / pow(m, n)

def pdf(n: int, m: int):
    return factorial(m) * stirling2(n - 1, m - 1) / pow(m, n)

print(stirling2(10, 9))


def cdf(number_of_cards: int):
    pass