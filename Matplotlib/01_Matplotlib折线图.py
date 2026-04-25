'''


'''

# 1- 导包
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 2- [可以省略]创建画布
    # 画布大小和dpi不要设置的过大，否则会出现图片展示失败。dpi一般设置100-150之间
    plt.figure(figsize=(10,20),dpi=150)

    # 3- 准备数据
    x_axis = [i for i in range(1,366)]
    y_axis = [np.random.randint(30,40) for i in range(1,366)]

    # 4- 绘制图形，折线图
    plt.plot(x_axis,y_axis)

    # 5- 展示图像
    plt.show()