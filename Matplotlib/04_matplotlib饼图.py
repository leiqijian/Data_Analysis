'''
matplotlib.pyplot.pie(data, lable)
'''
import matplotlib.pyplot as plt

# 中文乱码解决的固定套路
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 1- 准备数据
    data = [26, 35, 25, 15]
    labels = ["湖南省", "广东省", "河南省", "山东省"]

    # 2- 绘制图形
    # 普通的平面图形
    # plt.pie(x=data,labels=labels,autopct="%.2f%%")

    explode = (0, 0.1, 0, 0)  # 突出某一块
    plt.pie(data, explode=explode, labels=labels, autopct='%.2f%%', shadow=True, startangle=90)

    plt.show()