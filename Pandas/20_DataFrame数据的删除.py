'''
del是直接永久删除原df中的列【慎重使用】
drop是返回删除后的df或seires，原df或seires没有被修改
series unique 给某一列数据去重
'''
import pandas as pd

data = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk').head(5)
print(data)

df = data.copy()

# drop 返回一个新的dataframe值，删除数据不会修改原df对象
df1 = df.drop(0) #删除行索引为0的数据
df2 = df.drop([1],axis=0) #删除行索引为1的数据
df3 = df.drop([1,2,4],axis=0) #删除多行

print(df1)
print(df2)
print(df3)

df4 = df.drop(["country"], axis=1) #删除country一整列
df5 = df.drop(["GDP","year"], axis=1) #删除多列

print(df4)
print(df5)

del df["year"] #没有返回值，直接修改原dataframe
print(df)

# dataframe 去重
df6 = df.copy()
df7 = df6._append(df6).reset_index(drop=True) # 了解
print(df7.drop_duplicates())

