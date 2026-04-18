'''
累计统计函数：
    cumsum()
    cummax()
    cumprod()
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/stock_day.csv")
new_df = df.sort_index() # 重置索引， 从小到大
print(df)

print(new_df["p_change"].cumsum())  # 计算该列前n项的和
print(new_df["p_change"].cummax())  # 计算该列前n项的最大值
print(new_df["p_change"].cummin())  # 计算该列前n项的最小值