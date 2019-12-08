#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick

"""
赠券收集问题
"""

__author__ = 'Nick Yang'

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import logging
from coupon_collector_solver import CouponCollectorSolver


class Application(tk.Frame):

    def __init__(self, master=None):
        self.solver = None
        # 主窗口设置
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Coupon Collector's problem")
        self.master.iconbitmap('coupon.ico')  # 经反复实验，只有windows平台能改图标
        self.pack()
        self.center_window(800, 600)
        # 最上面空一行
        self.frame0 = tk.Frame(self.master)
        self.frame0.pack(side=tk.TOP, ipady=10)
        # 设置卡片种类数的滚动条
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack(side=tk.TOP, pady=3)
        self.label_annotation_n = tk.Label(self.frame1, text='number of types: ')
        self.label_annotation_n.pack(side=tk.LEFT)
        self.n = None
        self.scale_n = tk.Scale(self.frame1, from_=1, to=200, resolution=1, orient=tk.HORIZONTAL, length=300,
                                showvalue=0, variable=self.n, command=self.on_scale_n_change)
        self.scale_n.set(12)
        self.scale_n.pack(side=tk.LEFT)
        self.n = int(self.scale_n.get())
        self.label_n = tk.Label(self.frame1, width=4)
        self.label_n.pack(side=tk.LEFT)
        # 设置置信水平的滚动条
        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(side=tk.TOP, pady=3)
        self.label_annotation_confidence_level = tk.Label(self.frame2, text='confidence level: ')
        self.label_annotation_confidence_level.pack(side=tk.LEFT)
        self.confidence_level = None
        self.scale_confidence_level = tk.Scale(self.frame2, from_=0.01, to=0.99, resolution=0.01, orient=tk.HORIZONTAL,
                                               length=300, showvalue=0, variable=self.confidence_level,
                                               command=self.on_scale_confidence_level_change)
        self.scale_confidence_level.set(0.95)
        self.scale_confidence_level.pack(side=tk.LEFT)
        self.confidence_level = float(self.scale_confidence_level.get())
        self.label_confidence_level = tk.Label(self.frame2, width=4)
        self.label_confidence_level.pack(side=tk.LEFT)
        # 输入和输出间再空一行
        self.frame3 = tk.Frame(self.master)
        self.frame3.pack(side=tk.TOP, ipady=10)
        # 打印数学期望
        self.frame4 = tk.Frame(self.master)
        self.frame4.pack(side=tk.TOP, pady=3)
        self.label_annotation_expectation = tk.Label(self.frame4, text='expectation: ', width=20)
        self.label_annotation_expectation.pack(side=tk.LEFT)
        self.label_expectation = tk.Label(self.frame4, width=35)
        self.label_expectation.pack(side=tk.LEFT)
        # 打印方差
        self.frame5 = tk.Frame(self.master)
        self.frame5.pack(side=tk.TOP, pady=3)
        self.label_annotation_variance = tk.Label(self.frame5, text='     variance: ', width=20)
        self.label_annotation_variance.pack(side=tk.LEFT)
        self.label_variance = tk.Label(self.frame5, width=35)
        self.label_variance.pack(side=tk.LEFT)
        # 打印双侧置信区间
        self.frame6 = tk.Frame(self.master)
        self.frame6.pack(side=tk.TOP, pady=3)
        self.label_annotation_two_sided_confidence_interval = tk.Label(self.frame6,
                                                                       text='two sided confidence interval: ', width=25)
        self.label_annotation_two_sided_confidence_interval.pack(side=tk.LEFT)
        self.label_two_sided_confidence_interval = tk.Label(self.frame6, width=30)
        self.label_two_sided_confidence_interval.pack(side=tk.LEFT)
        # 打印单侧置信区间
        self.frame7 = tk.Frame(self.master)
        self.frame7.pack(side=tk.TOP, pady=3)
        self.label_annotation_one_sided_confidence_interval = tk.Label(self.frame7,
                                                                       text='one sided confidence interval: ', width=25)
        self.label_annotation_one_sided_confidence_interval.pack(side=tk.LEFT)
        self.label_one_sided_confidence_interval = tk.Label(self.frame7, width=30)
        self.label_one_sided_confidence_interval.pack(side=tk.LEFT)
        # 概率密度函数和累积分布函数绘制区
        self.frame8 = tk.Frame(self.master)
        self.frame8.pack(side=tk.TOP, pady=3)
        self.pdf_and_cdf = Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.pdf_and_cdf, master=self.frame8)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas.draw()

    def on_scale_n_change(self, n: int):
        self.n = int(n)
        self.label_n['text'] = str(self.n)
        self.solver = CouponCollectorSolver(self.n)
        self.label_expectation['text'] = str(self.solver.expectation)
        self.label_variance['text'] = str(self.solver.variance)
        self.update_interval()
        # 清空画布
        self.pdf_and_cdf.clf()
        # 准备绘制概率密度函数
        pdf = self.pdf_and_cdf.add_subplot(121)
        pdf.scatter(self.solver.horizontal_axis, self.solver.all_pdf, s=1)
        pdf.set_title('probability density function')
        pdf.set_xlabel('times of selections')
        pdf.set_ylabel('probability')
        pdf.set_xlim(0, self.solver.max_pdf_cdf_t)
        pdf.set_ylim(0)
        # 准备绘制累积分布函数
        cdf = self.pdf_and_cdf.add_subplot(122)
        cdf.scatter(self.solver.horizontal_axis, self.solver.all_cdf, s=1)
        cdf.set_title('cumulative distribution function')
        cdf.set_xlabel('times of selections')
        cdf.set_ylabel('probability')
        cdf.set_xlim(0, self.solver.max_pdf_cdf_t)
        cdf.set_ylim(0, 1)
        # 真正画上去
        self.canvas.draw()
        # 把计算结果输出到控制台，方便用户复制结果
        logging.info('number of types: ' + self.label_n['text'])
        logging.info('expectation: ' + self.label_expectation['text'])
        logging.info('variance: ' + self.label_variance['text'])

    def on_scale_confidence_level_change(self, confidence_level: float):
        self.confidence_level = float(confidence_level)
        self.label_confidence_level['text'] = '{:.0%}'.format(self.confidence_level)
        self.update_interval()

    def update_interval(self):
        if self.solver:
            interval = self.solver.two_sided_confidence_interval(self.confidence_level)
            self.label_two_sided_confidence_interval['text'] = '(%d, %d)' % (interval[0], interval[1])
            self.label_one_sided_confidence_interval['text'] = \
                '(0, %d) or (%d, math.inf)' % (self.solver.one_sided_upper_confidence_limit(self.confidence_level),
                                               self.solver.one_sided_lower_confidence_limit(self.confidence_level))
            # 把计算结果输出到控制台，方便用户复制结果
            logging.info('confidence level: {:.0%}'.format(self.confidence_level))
            logging.info('two sided confidence interval: ' + self.label_two_sided_confidence_interval['text'])
            logging.info('one sided confidence interval: ' + self.label_one_sided_confidence_interval['text'])

    def center_window(self, w: int, h: int):
        """
        屏幕居中
        :param self: 自身
        :param w: 窗口宽度
        :param h: 窗口高度
        :return: 无
        """
        # 获取屏幕 宽、高
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
