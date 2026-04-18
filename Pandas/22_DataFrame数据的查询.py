'''
dataframe的查询API
    1. 前从后取多行数据
    2. 获取一列或多列数据
    3. 索引下标切片取行
    4. 查询函数获取子集: df.query()
    5. 排序函数
    6. 聚合函数
'''

import pandas as pd

data = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk').head(5)
print(data)

df = data.copy()

# 1. 前从后取多行数据
# 默认取前5行数据
df.head()
df.head(10) # 取前10行
# 默认取后5行数据
df.tail()
df2 = df.tail(15) # 倒数15行

# 2. 获取一列或多列数据
# 获取一列数据`df[col_name]`等同于`df.col_name`
# 获取多列数据`df[[col_name1,col_name2,...]]`
print(df2['country']) #返回series对象
print(df2.country) #返回series对象
print(df2[['country', 'GDP']]) #返回新的df

# 3. 索引下标切片取行
# df[start:stop:step]
# df[起始行下标:结束行下标:步长]
# 遵循 顾头不顾尾 原则（包含起始行，不包含结束行），步长默认为1
df = df.head(10) # 取原df前10行数据作为df4，默认自增索引由0到9
print(df[0:3]) # 从头开始取到第2行
print(df[:5:2]) #从头开始取，取到第4行，步长为2
print(df[1::3]) #从1开始取，取到结尾，步长为3

# 4. 查询函数获取子集: df.query()
print(df.query('country=="美国"'))
print(df[df['country'] == '美国'])
print(df.query('country=="中国" or country=="日本" or country=="美国"').query(
    'year in ["2015", "2016", "2017", "2018", "2019"]'))

# 5. 排序函数
# sort_values函数: 按照指定的一列或多列的值进行排序
# 按GDP列的数值由小到大进行排序
df.sort_values(['GDP'])
# 按GDP列的数值由大到小进行排序
df.sort_values(['GDP'], ascending=False) # 倒序， ascending默认为True
# 先对year年份进行由小到大排序，再对GDP由小到大排序
df.sort_values(['year', 'GDP'])

# 6. 聚合函数:
# - min 最小值
# - max 最大值
# - mean 平均值
# - sum 求和
# - count  求个数

