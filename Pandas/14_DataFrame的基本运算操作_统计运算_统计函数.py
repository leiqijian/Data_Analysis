'''
统筹运算：
        
'''

import pandas as pd
import numpy as np

data = pd.read_csv('data/stock_day.csv')

print(data)

# 对数据的整体情况进行统计：计数、均值、标准差、分位数、最小最大
print(data.describe())

print("------")
# data.max(0) 的意思是：计算 DataFrame 中每一列的最大值，并返回一个包含每列最大值的 Series
print(data.max(0))

# data.max(1) 的意思是：计算 DataFrame 中每一行的最大值，并返回一个包含每行最大值的 Series
print(data.max(axis=1))

print("------")

df = pd.DataFrame({'COL1' : [2,3,4,5,4,2], 'COL2' : [0,1,2,3,4,2]})
print(df)

print(df['COL2'].std()) #计算open 这一列的标准差
print(df['COL2'].var()) #计算open 这一列的方差

print(df['COL2'].median()) #计算open 这一列的中位数

# idxmax 取最大值的索引
print(df['COL1'].idxmax(axis=0)) # 取COL1 这一列的最大值对应的索引
print(df['COL2'].idxmax(axis=0)) # 取COL2 这一列的最大值对应的索引


