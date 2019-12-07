#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick


"""
赠券收集问题
"""

from coupon_collector_solver import CouponCollectorSolver


solver = CouponCollectorSolver(12)
for i in range(110):
    print(str(i) + " " + str(solver.cdf(i)))
print(solver.one_sided_lower_confidence_limit(0.95))
print(solver.one_sided_upper_confidence_limit(0.95))
print(solver.two_sided_confidence_interval(0.90))
