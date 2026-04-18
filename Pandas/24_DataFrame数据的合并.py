'''
DataFrame 数据合并
    1. concat()
    2. merge() 相当于是MySQL中的join操作
'''

import pandas as pd
import numpy as np

df = pd.read_csv("data/1960-2019全球GDP数据.csv",encoding="GBK")
df1 = df.copy()

# 1.concat拼接
# axis=1：行数不变，列数增加
df2 = pd.concat(objs=[df1,df1], axis=1)
print(df2)

# axis=0：列数不变，行数增加
df3 = pd.concat(objs=[df1,df1,df1,df1], axis=0)
print(df3)


# 2. merge拼接
# 自定义数据
data_A = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

data_B = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

# how : {"inner" , "left" , "right" , "outer"}
df = pd.merge(left=data_A, right=data_B, how="inner", on=['key1', 'key2'])
print(df)

"""
    select
        *
    from left 
    left join 
    right 
    on left.key1=right.key1 and left.key2=right.key2
"""
df = pd.merge(left=data_A,right=data_B,how="left",on=['key1', 'key2'])
print(df)