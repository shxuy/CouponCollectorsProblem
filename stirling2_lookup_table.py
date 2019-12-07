# -*- coding: utf-8 -*-
#
# @author Nick

"""
一口气算完 (n + 1) * (m + 1) 个第二类Stirling数，然后查阅使用，避免重复计算
"""


class Stirling2LookupTable(object):

    def __init__(self, n_max: int, m_max: int):
        if not isinstance(n_max, int):
            raise TypeError('the parameter n_max should be a natural number')
        if n_max < 0:
            raise ValueError('the parameter n_max should be a natural number')
        if not isinstance(m_max, int):
            raise TypeError('the parameter m_max should be a natural number')
        if m_max < 0:
            raise ValueError('the parameter m_max should be a natural number')
        self.__n_max = n_max
        self.__m_max = m_max
        # 我一开始使用 np.zeros((n_max + 1, m_max + 1), dtype=int) 来初始化 self.__table，可惜当 n_max 和 m_max 足够大
        # （比如 n_max 和 m_max 分别为30）时，表中的数字会溢出。
        self.__table = [[0 for x in range(m_max + 1)] for y in range(n_max + 1)]
        self.__table[0][0] = 1
        if self.__m_max >= 1:
            for i in range(1, self.__n_max + 1):
                self.__table[i][1] = 1
        for i in range(2, self.__m_max + 1):
            for j in range(i, self.__n_max + 1):
                self.__table[j][i] = self.__table[j - 1][i - 1] + self.__table[j - 1][i] * i

    @property
    def n_max(self):
        return self.__n_max

    @property
    def m_max(self):
        return self.__m_max

    def stirling2(self, n: int, m: int):
        if not isinstance(n, int):
            raise TypeError('the parameter n should be an integer')
        if n < 0 or n > self.__n_max:
            raise ValueError('the parameter n should be >= 0 and <= %d' % self.__n_max)
        if not isinstance(m, int):
            raise TypeError('the parameter m should be an integer')
        if m < 0 or m > self.__m_max:
            raise ValueError('the parameter m should be >= 0 and <= %d' % self.__m_max)
        return self.__table[n][m]

    def __str__(self):
        return '[' + ',\n'.join([str(x) for x in self.__table]) + ']'
