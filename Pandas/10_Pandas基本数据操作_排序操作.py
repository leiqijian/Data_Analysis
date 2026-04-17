'''
1- 索引操作
	loc[行索引名称开始:行索引名称结束, 列索引名称开始:列索引名称结束]，注意左右都是闭区间
	iloc[行索引下标开始:行索引下标结束, 列索引下标开始:列索引下标结束]，注意左闭右开

2- 赋值操作
	DataFrame对象['字段名称'] = 字段值

3- 排序操作
	sort_index()
'''

import pandas as pd
import numpy as np

# display.max_columns : 最大显示列数，None 表示不限制
# display.max_rows : 最大显示行数，None 表示不限制
# display.width : 控制台总宽度，None 表示不限制
# display.max_colwidth : 每列最大字符宽度，None 表示不限制
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
data = pd.read_csv('data/stock_day.csv')
print(data.head())

# 按照 open字段进行升序排序
# by: 指定排序的键
# ascending：默认true升序，false，降序
# print(data.sort_values(by="open", ascending=True).head())

# 按照多个键进行排序. 先按open排，open相同再按high排
# print(data.sort_values(by=['open', 'high']).head())

# 对索引进行排序,原来是从大到小，改为从小到大
# print(data.sort_index().head())

# 对series对象进行排序
# print(data['p_change'].sort_values(ascending=True).head())

# 对series对象进行索引重新排序
print(data['p_change'].sort_index().head())



