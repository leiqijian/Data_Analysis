import matplotlib.pyplot as plt
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# Mac电脑用下面的代码
# mpl.rcParams["font.sans-serif"] = ['PingFang SC', 'SimHei']
# 有时候，字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要更改axes.unicode_minus参数：
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 1- 创建画布
    plt.figure(figsize=(10,20),dpi=150)

    # 2- 准备数据
    x = ["江西省", "广东省", "河南省", "湖南省"]
    y = [10, 20, 13, 16]

    # 3- 绘制图形
    plt.bar(x=x,height=y)

    # 4- 其他信息设置
    plt.title("各个省份的学生人数")  # 图形的标题
    plt.xlabel("省份")    # 横轴名称
    plt.ylabel("人数")    # 纵轴名称

    plt.show()