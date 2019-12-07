# -*- coding: utf-8 -*-
#
# @author Nick

"""
计算赠券收集问题的数学期望、方差、概率密度函数和累积分布函数
"""

import math
from stirling2_lookup_table import Stirling2LookupTable


class CouponCollectorSolver(object):

    def __init__(self, n: int):
        """
        初始化
        :param n: 卡片种类数
        """
        if not isinstance(n, int):
            raise TypeError('the parameter n should be a natural number')
        if n < 0:
            raise ValueError('the parameter n should be a natural number')
        self.__n = n
        self.__max_pdf_cdf_t = int(self.expectation * 2)  # 概率密度函数和累计分布函数的自变量最大值，两倍于数学期望应该够了
        self.__table = Stirling2LookupTable(self.__max_pdf_cdf_t, self.__n)

    @property
    def n(self):
        return self.__n

    @property
    def expectation(self):
        """
        返回数学期望
        :return: 数学期望: float
        """
        sum = 0
        for i in range(1, self.__n + 1):
            sum += self.__n / i
        return sum

    @property
    def variance(self):
        """
        返回方差
        :return: 方差: float
        """
        sum = 0
        for i in range(1, self.__n + 1):
            sum += self.__n * self.__n / (i * i) - self.__n / i
        return sum

    def pdf(self, t: int):
        """
        概率密度函数
        :param t: 抽取次数
        :return: 概率密度函数: float
        """
        if not isinstance(t, int):
            raise TypeError('the parameter t should be a natural number')
        if t < 0 or t > self.__max_pdf_cdf_t:
            raise ValueError('the parameter t should be >= 0 and <= %d' % self.__max_pdf_cdf_t)
        if self.__n == 0 or t == 0:
            return 0.0
        return math.factorial(self.__n) * self.__table.stirling2(t - 1, self.__n - 1) / pow(self.__n, t)

    def cdf(self, t: int):
        """
        累积分布函数
        :param t: 抽取次数
        :return: 累积分布函数: float
        """
        if not isinstance(t, int):
            raise TypeError('the parameter t should be a natural number')
        if t < 0 or t > self.__max_pdf_cdf_t:
            raise ValueError('the parameter t should be >= 0 and <= %d' % self.__max_pdf_cdf_t)
        return math.factorial(self.__n) * self.__table.stirling2(t, self.__n) / pow(self.__n, t)
