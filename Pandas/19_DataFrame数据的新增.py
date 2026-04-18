'''
1- 增加新字段
DataFrame对象["新字段名称"] = 字段值
'''

import pandas as pd

data = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk').head(5)
print(data)

# 方式一: 通过直接赋值的方式添加新列
df = data.copy()

df["new_f1"] = 666
print(df)

df["new_f2"] = [11, 22, 33, 44, 55]
print(df)

df["new_f3"] = df.year * 100
print(df)

# 方式二： dataframe.assign函数
# assign特殊
def fn1(my_df):
    return 22

def fn2(my_df):
    return my_df.GDP/1000000+my_df.year

df_5 = df.assign(
    new1=100,
    new2=[11,22,33,44,55],
    new3=df.year*100,
    new4=fn1,
    new5=fn2
)
print(df_5)