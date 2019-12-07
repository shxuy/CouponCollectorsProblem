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
        self.__max_pdf_cdf_t = int(self.expectation * 3)  # 概率密度函数和累积分布函数的自变量最大值，三倍于数学期望应该够了
        self.__table = Stirling2LookupTable(self.__max_pdf_cdf_t, self.__n)
        self.__cdf_series = None

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
    def max_pdf_cdf_t(self):
        """
        返回概率密度函数和累积分布函数的自变量最大值
        :return: 概率密度函数和累积分布函数的自变量最大值: int
        """
        return self.__max_pdf_cdf_t

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

    @property
    def horizontal_axis(self):
        """
        所有概率密度函数值或所有累积分布函数值对应的横坐标轴
        :return: 一个由self.__max_pdf_cdf_t + 1个int组成的list
        """
        return list(range(self.__max_pdf_cdf_t + 1))

    @property
    def all_pdf(self):
        """
        区间[0, self.__max_pdf_cdf_t]上的所有概率密度函数值
        :return: 一个由self.__max_pdf_cdf_t + 1个float组成的list
        """
        return [self.pdf(x) for x in range(self.__max_pdf_cdf_t + 1)]

    @property
    def all_cdf(self):
        """
        区间[0, self.__max_pdf_cdf_t]上的所有累积分布函数值
        :return: 一个由self.__max_pdf_cdf_t + 1个float组成的list
        """
        return [self.cdf(x) for x in range(self.__max_pdf_cdf_t + 1)]

    def two_sided_confidence_interval(self, confidence_level: float):
        """
        双侧置信区间，即置信区间为(lower_bound, upper_bound)
        :param confidence_level: 置信水平
        :return: 双侧置信区间，形式为一个包括两个int的list
        """
        if not isinstance(confidence_level, float):
            raise TypeError('the parameter confidence_level should be a float number')
        if confidence_level <= 0 or confidence_level >= 1:
            raise ValueError('the parameter confidence_level should be > 0 and < 1')
        alpha = 1 - confidence_level
        self.__calculate_all_cdf()
        lower_bound = self.__binary_search_largest_value(self.__cdf_series, alpha / 2)
        upper_bound = self.__binary_search_smallest_value(self.__cdf_series, 1 - alpha / 2)
        return [lower_bound, upper_bound]

    def one_sided_lower_confidence_limit(self, confidence_level: float):
        """
        单侧置信下限，即置信区间为(lower_bound, math.inf)
        :param confidence_level: 置信水平
        :return: 单侧置信下限lower_bound: int
        """
        if not isinstance(confidence_level, float):
            raise TypeError('the parameter confidence_level should be a float number')
        if confidence_level <= 0 or confidence_level >= 1:
            raise ValueError('the parameter confidence_level should be > 0 and < 1')
        self.__calculate_all_cdf()
        alpha = 1 - confidence_level
        lower_bound = self.__binary_search_largest_value(self.__cdf_series, alpha)
        return lower_bound

    def one_sided_upper_confidence_limit(self, confidence_level: float):
        """
        单侧置信上限，即置信区间为(0, upper_bound)
        :param confidence_level: 置信水平
        :return: 单侧置信上限upper_bound: int
        """
        if not isinstance(confidence_level, float):
            raise TypeError('the parameter confidence_level should be a float number')
        if confidence_level <= 0 or confidence_level >= 1:
            raise ValueError('the parameter confidence_level should be > 0 and < 1')
        self.__calculate_all_cdf()
        upper_bound = self.__binary_search_smallest_value(self.__cdf_series, confidence_level)
        return upper_bound

    def __calculate_all_cdf(self):
        """
        计算区间[0, self.__max_pdf_cdf_t]上的所有累积分布函数值
        :return: 无
        """
        if not self.__cdf_series:
            self.__cdf_series = [self.cdf(x) for x in range(self.__max_pdf_cdf_t + 1)]

    @staticmethod
    def __binary_search_largest_value(array: list, lookup_value: float):
        """
        二分查找。查找小于或等于 lookup_value 的最大值对应的序号
        :param array: 一个升序序列
        :param lookup_value: 查找的值
        :return: 序号
        """
        low = 0
        high = len(array) - 1
        while low <= high:
            middle = low + (high - low) // 2
            middle_value = array[middle]
            if lookup_value > middle_value:
                low = middle + 1
            elif lookup_value < middle_value:
                high = middle - 1
            else:
                return middle
        return high

    @staticmethod
    def __binary_search_smallest_value(array: list, lookup_value: float):
        """
        二分查找。查找大于或等于 lookup_value 的最小值对应的序号
        :param array: 一个升序序列
        :param lookup_value: 查找的值
        :return: 序号
        """
        low = 0
        high = len(array) - 1
        while low <= high:
            middle = low + (high - low) // 2
            middle_value = array[middle]
            if lookup_value > middle_value:
                low = middle + 1
            elif lookup_value < middle_value:
                high = middle - 1
            else:
                return middle
        return low
