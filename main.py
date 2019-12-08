#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick

"""
赠券收集问题
"""

__author__ = 'Nick Yang'

'''
import sys
import traceback
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from coupon_collector_solver import CouponCollectorSolver


def pdf_and_cdf(solver):
    """
    根据一个赠券收集问题解算实例，绘制概率密度函数和累积分布函数
    :param solver: 赠券收集问题解算实例
    :return: 一个包含概率密度函数和累积分布函数的matplotlib.figure
    """
    figure = Figure(figsize=(8, 4))
    # 绘制概率密度函数
    pdf = figure.add_subplot(121)
    pdf.plot(solver.horizontal_axis, solver.all_pdf, '.b')
    plt.title('probability density function')
    plt.xlabel('times of selections')
    plt.ylabel('probability')
    plt.xlim(0, solver.max_pdf_cdf_t)
    plt.ylim(0)
    # 绘制累积分布函数
    cdf = figure.add_subplot(122)
    cdf.plot(solver.horizontal_axis, solver.all_cdf, '.b')
    plt.title('cumulative distribution function')
    plt.xlabel('times of selections')
    plt.ylabel('probability')
    plt.xlim(0, solver.max_pdf_cdf_t)
    plt.ylim(0, 1)
    return figure


def main(argv):
    solver = CouponCollectorSolver(12)
    figure = pdf_and_cdf(solver)
    figure.show()
    print(solver.one_sided_lower_confidence_limit(0.95))
    print(solver.one_sided_upper_confidence_limit(0.95))
    print(solver.two_sided_confidence_interval(0.90))


if __name__ == '__main__':
    try:
        exit(main(sys.argv[1:]))
    except TypeError or ValueError or Exception:
        traceback.print_exc()




root = tkinter.Tk()
root.wm_title("coupon collector's problem")

# 画布的大小和分别率
fig = Figure(figsize=(10, 4))

# 利用子图画图
axc = fig.add_subplot(121)
axc.plot([1, 2, 3, 4, 5], "ob")

# 创建画布控件
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
# 显示画布控件
canvas.get_tk_widget().pack()

# 创建工具条控件
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
# 显示工具条控件
#canvas.get_tk_widget().pack()


# 绑定快捷键函数
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


# 调用快捷键函数
canvas.mpl_connect("key_press_event", on_key_press)


# 退出函数
def _quit():
    root.quit()
    root.destroy()


# 消息循环
tkinter.mainloop()
'''
'''
import numpy as np
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from coupon_collector_solver import CouponCollectorSolver


def drawPic():
    fig.clf()
    # 绘制概率密度函数
    pdf = fig.add_subplot(121)
    pdf.scatter(solver.horizontal_axis, solver.all_pdf, s=1)
    pdf.set_title('probability density function')
    pdf.set_xlabel('times of selections')
    pdf.set_ylabel('probability')
    pdf.set_xlim(0, solver.max_pdf_cdf_t)
    pdf.set_ylim(0)
    # 绘制累积分布函数
    cdf = fig.add_subplot(122)
    cdf.scatter(solver.horizontal_axis, solver.all_cdf, s=1)
    cdf.set_title('cumulative distribution function')
    cdf.set_xlabel('times of selections')
    cdf.set_ylabel('probability')
    cdf.set_xlim(0, solver.max_pdf_cdf_t)
    cdf.set_ylim(0, 1)
    fig_canvas.draw()



if __name__ == '__main__':
    solver = CouponCollectorSolver(12)
    root = tkinter.Tk()
    tkinter.Label(root, text='number of types: ').grid(row=0, column=0)
    inputEntry = tkinter.Entry(root)
    inputEntry.grid(row=0, column=1)
    inputEntry.insert(0, '12')
    tkinter.Button(root, text='draw', command=drawPic).grid(row=0, column=2, columnspan=3)
    fig = Figure(figsize=(8, 4), dpi=100)
    fig_canvas = FigureCanvasTkAgg(fig, master=root)
    fig_canvas.get_tk_widget().grid(row=1, columnspan=3)

    #启动事件循环
    root.mainloop()
    
'''
import tkinter as tk
from coupon_collector_solver import CouponCollectorSolver


class Application(tk.Frame):

    def __init__(self, master=None):
        self.solver = None
        # 主窗口设置
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Coupon Collector's problem")
        self.pack()
        self.center_window(500, 500)
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

    def on_scale_n_change(self, n: int):
        self.n = int(n)
        self.label_n['text'] = str(self.n)
        self.solver = CouponCollectorSolver(self.n)
        self.label_expectation['text'] = str(self.solver.expectation)
        self.label_variance['text'] = str(self.solver.variance)
        self.update_interval()

    def on_scale_confidence_level_change(self, confidence_level: float):
        self.confidence_level = float(confidence_level)
        self.label_confidence_level['text'] = '{:.0%}'.format(self.confidence_level)
        self.update_interval()

    def update_interval(self):
        interval = self.solver.two_sided_confidence_interval(self.confidence_level)
        self.label_two_sided_confidence_interval['text'] = '(%d, %d)' % (interval[0], interval[1])
        self.label_one_sided_confidence_interval['text'] = \
            '(0, %d) or (%d, math.inf)' % (self.solver.one_sided_upper_confidence_limit(self.confidence_level),
                                           self.solver.one_sided_lower_confidence_limit(self.confidence_level))

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
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
