import matplotlib.pyplot as plt
import random

# 设置显示中文字体
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

if __name__ == '__main__':
    # 1- 准备数据
    x = range(60)
    # random.uniform(15,18):随机生成15到18之间的随机数.如果随机数很多的时候,这些数据满足均匀分布
    y_guangzhou = [random.uniform(15, 18) for i in x]
    y_shanghai = [random.uniform(5, 8) for i in x]

    # 2- 创建画布
    plt.figure(figsize=(20,20),dpi=150)

    # 3- 绘制图形
    plt.plot(x, y_guangzhou, label="广州")
    plt.plot(x, y_shanghai, label="上海")

    # 4- 添加辅助信息
    # 4.1- 网格线
    plt.grid(visible=True,linestyle=":",color="pink",alpha=0.5)

    # 4.2- 刻度尺
    x_ticks_name = [f"11点{i}分" for i in x]
    y_ticks = range(40)

    # ticks的个数必须与labels的个数一致
    # [::5] 从头取到尾,步长是5
    plt.xticks(ticks=x[::5],labels=x_ticks_name[::5])

    # xticks和yticks没有任何关系
    plt.yticks(ticks=y_ticks)

    # 4.3- 标题信息
    # 添加x轴、y轴描述信息及标题
    plt.xlabel("时间")
    plt.ylabel("温度")
    # fontsize:字体大小,值越大字就越大
    plt.title("中午11点0分到12点之间的温度变化图示", fontsize=20)

    # 4.4- 图例
    # legend：展示图例
    # loc="upper right"：将图例放在右上角
    plt.legend(loc="upper right")

    # 4.5- 保存图片
    # 注意:保存图片需要在show之前执行,否则图片中没有内容
    plt.savefig("data/图形演示.jpg")

    plt.show()
