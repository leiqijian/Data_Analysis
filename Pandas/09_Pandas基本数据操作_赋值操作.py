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

#对DataFrame当中的close open 列进行重新赋值为1
#两种方法改变一整列的值
data["close"] = 1

data.open = 1

print(data.head())
