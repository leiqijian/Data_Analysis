'''
分组
    -

查询
    -

聚合函数
    -

分组聚合的过滤操作
    -
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



