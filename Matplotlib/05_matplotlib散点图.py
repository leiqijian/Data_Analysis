'''
matplotlib.pyplot.scatter(X, Y)
'''

import matplotlib.pyplot as plt
# 中文乱码解决的固定套路
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 有时候，字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要更改axes.unicode_minus参数：
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 准备数据
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # 绘制散点图
    plt.scatter(x, y, color="red", alpha=0.7)

    # 设置标题
    plt.title("散点图案例")
    plt.xlabel("x轴")
    plt.ylabel("y轴")

    # 展示
    plt.show()