#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Nick


"""
赠券收集问题
"""
from matplotlib import pyplot as plt
from coupon_collector_solver import CouponCollectorSolver

solver = CouponCollectorSolver(12)
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.plot(solver.horizontal_axis, solver.all_pdf, '.b')
plt.title('probability density function')
plt.xlabel('times of selections')
plt.ylabel('probability')
plt.xlim(0, solver.max_pdf_cdf_t)
plt.ylim(0)
plt.subplot(122)
plt.plot(solver.horizontal_axis, solver.all_cdf, '.b')
plt.title('cumulative distribution function')
plt.xlabel('times of selections')
plt.ylabel('probability')
plt.xlim(0, solver.max_pdf_cdf_t)
plt.ylim(0, 1)
plt.show()

print(solver.one_sided_lower_confidence_limit(0.95))
print(solver.one_sided_upper_confidence_limit(0.95))
print(solver.two_sided_confidence_interval(0.90))
'''
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("赠券收集问题")

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