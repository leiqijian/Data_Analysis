'''
1. df.assign替换列
2. 直接对原始数据进行赋值修改
3. replace函数替换数据
'''

import pandas as pd

data = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk').head(5)
# print(data)

df = data.copy()

# 直接对原始的DF进行赋值修改处理
df["GDP"] = [5, 4, 3, 2, 1]

print(df)

# replace函数替换数据
# series对象替换数据，返回的还是series对象，不会对原来的df造成修改
# 参数解释：inplace=True，直接对原始数据进行修改
series = df.year.replace(1960, 19600)

print(df)
print(series)
print(type(series))  #<class 'pandas.core.series.Series'>

# 如果加上inplace=True参数，则会修改原始df
df.country.replace('日本', '扶桑', inplace=True)

print(df)

# df也可以直接调用replace函数，用法和s.replace用法一致，只是返回的是df对象
df.replace(1960, 19600)
print(df)
