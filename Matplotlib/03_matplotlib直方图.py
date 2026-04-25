import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# Mac电脑用下面的代码
# mpl.rcParams["font.sans-serif"] = ['PingFang SC', 'SimHei']
# 有时候，字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要更改axes.unicode_minus参数：
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 1- 创建画布
    plt.figure(figsize=(10, 20), dpi=150)

    # 2- 准备数据
    data = np.random.randn(500)

    # 3- 绘制图形
    """
        参数解释：
            x：要展示的数据
            bins：将数据分为多少个区间
            rwidth：将横轴的多少区域用来绘制图形。例如：0.8，80%的区域用来绘制柱状图，20%是空白的
            color：柱子的颜色
            alpha：颜色的透明度。值越小，也就是颜色越淡

        柱子的高度由什么决定？
            1- 找出x数据中的min最小值和max最大值
            2- bins表示将数据分为多少个区间。(max-min)/bins表示每个区间的上限和下限的差值是多少
                举例：max=200，min=80，bins=60，计算结果是(200-80)/60=2  
                那么第一个区间的范围[80,80+2)
                那么第二个区间的范围[82,80+2+2)
                ...
            3- 然后将x中的数据，根据上面的区间进行数据个数的统计。统计出来的个数，就是柱子的高度
    """
    plt.hist(x=data, bins=60, rwidth=0.8, color="red", alpha=0.4)

    plt.title("这是一个直方图")
    plt.xlabel("值范围")
    plt.ylabel("高度")
    plt.show()