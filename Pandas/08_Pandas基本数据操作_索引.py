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
# print(data)
print(type(data))


# axis = 1 :修改列
# axis = 0 :修改行
# 1. 删除 行列 操作
data = data.drop(["ma5", "ma10"], axis=1)
# print(data.head())

# 2. 通过 行列 索引查询值 (先列后行)
# 2.1
print(data["ma20"]["2018-02-26"])

# 2.2 通过loc属性拿到对应值 先行后列
# 语法总结：[行索引开始名称:行索引结束名称, 列索引开始名称:列索引结束名称]，注意左右都是闭区间
print(data.loc["2018-02-26"]["ma20"])

# 2.3 范围取值
print(data.loc["2018-02-26":"2018-02-22", "volume"])

print(data.loc["2018-02-26":"2018-02-23", "close":"low"])

# 2.4 通过iloc和行列索引下标取内容 先行后列
# 语法总结：[行索引开始下标:行索引结束下标, 列索引开始下标:列索引结束下标]，注意左闭右开
print(data.iloc[2, 1])

print(data.iloc[2, 1:3])

print(data.iloc[1:3, 1:4])