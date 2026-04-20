'''
分组
    -dataframe.groupby() return 分组对象
        - 基于一列进行分组 df.groupby(['gender_group'])
        - 基于多列进行分组 df.groupby(['gender_group', 'city'])

查询
    - DataFrameGroupBy对象.first() # 取出每组第一条数据
    - DataFrameGroupBy对象.last() # 取出每组最后一条数据
    - DataFrameGroupBy对象.get_group() # 按分组依据获取其中一组

聚合函数
    :分组后对多列分别使用不同的聚合函数
        -dataframe.groupby().agg({'指定列1':'聚合函数名',  '指定列2':'聚合函数名'})

分组聚合的过滤操作
    : 返回分组之后满足过滤条件的组的所有数据
        - dataframe.groupby(['列名1',...]).filter(lambda s: s.mean() > 200)
'''

import pandas as pd
import numpy as np

df = pd.read_csv('data/uniqlo.csv')

print(df.head())

gender_group = df.groupby('gender_group')
# gender_group = df.groupby(['gender_group'])


print(gender_group) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000022D8A697230>

gender_group = df.groupby(['gender_group', 'channel'])

print(gender_group.first())
print(gender_group.last())

print(gender_group.get_group(('Female', '线上')))

print(gender_group.get_group(('Female', '线上')).agg(
    {
        'revenue' :'max',
        'unit_cost' : 'sum'
    }
))

# 过滤操作
print(df.groupby('city').filter(lambda d: d['revenue'].mean() > 200))

print(df.groupby('city').aggregate({'revenue': 'mean'}).query('revenue > 200'))



