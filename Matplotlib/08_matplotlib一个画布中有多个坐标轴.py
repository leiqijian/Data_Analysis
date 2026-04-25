import matplotlib.pyplot as plt
import random

from matplotlib.axes import Axes
# 设置显示中文字体
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 1- 准备数据
    x = range(60)
    y_guangzhou = [random.uniform(15, 18) for i in x]
    y_shanghai = [random.uniform(5, 8) for i in x]

    # 2- 创建画布：将画布分为1行2列，有2个区域的格子
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10), dpi=150)

    # 对变量进行类型声明，作用是为了后面写代码有提示
    axes_0: Axes = axes[0]
    axes_1: Axes = axes[1]

    # 3- 绘制图形
    # axes[0]：表示在第一个格子中绘制图形。索引从0开始
    axes_0.plot(x, y_guangzhou, label="广州")
    axes_1.plot(x, y_shanghai, label="上海")

    # 4- 辅助信息
    # 4.1- 网格线
    axes_0.grid(visible=True, linestyle=":", color="blue", alpha=0.9)
    axes_1.grid(visible=True, linestyle="--", color="red", alpha=0.9)

    # 4.2- 图例
    axes_0.legend(loc="upper right")
    axes_1.legend(loc="upper left")

    # 4.3- 刻度尺
    x_ticks_name = [f"11点{i}分" for i in x]
    y_ticks = range(40)

    # 广州
    axes_0.set_xticks(x[::5], x_ticks_name[::5])
    axes_0.set_yticks(y_ticks[::5])

    # 上海
    # shift+alt+鼠标左键
    axes_1.set_xticks(x[::5], x_ticks_name[::5])
    axes_1.set_yticks(y_ticks[::5])

    # 4.4- 标题
    axes_0.set_xlabel("时间")
    axes_0.set_ylabel("温度")
    axes_0.set_title("广州市_中午11点0分到12点之间的温度变化图示", fontsize=20)

    axes_1.set_xlabel("时间")
    axes_1.set_ylabel("温度")
    axes_1.set_title("上海市_中午11点0分到12点之间的温度变化图示", fontsize=20)

    plt.show()