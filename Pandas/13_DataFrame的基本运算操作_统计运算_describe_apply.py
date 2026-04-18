'''
统筹运算：
        describe() :综合分析: 能够直接得出很多统计结果,`count`, `mean`, `std`, `min`, `max` 等
        apply(func, axis=0)
            - func : 自定义函数
            - axis : 默认是0. 以列进行计算，如果设置为1. 则以行进行计算
'''

import pandas as pd
import numpy as np

data = pd.read_csv("data/stock_day.csv")

print(data)

print(data.describe())

print(data["open"].describe())
print(data.loc["2018-02-27"].describe())

# open     22.74
# close    22.85
# dtype: float64
# 统计open，close这两列，最大最小值之间的差值是多少
print(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0))

# 统计open，close这两列，每一行之间的差距是多少, 绝对值
print(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=1))



