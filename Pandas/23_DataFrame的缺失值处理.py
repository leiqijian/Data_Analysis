
'''
缺失值的标记方式是NaN

- 判断数据中是否包含NaN：
  - pd.isnull(df) return df
  - pd.notnull(df) return df
  - numpy.all(df) return boolean
  - numpy.any(df) return boolean
- 存在缺失值nan:
  - 1、删除存在缺失值的:
    - dropna(axis)
    - 注：不会修改原数据，需要接受返回值
  - 2、替换缺失值:
    - fillna(value, inplace=True)
        - value:替换成的值
        - inplace:True:会修改原数据，False:不替换修改原数据，生成新的对象
  - 3、异常值不是NaN。需要先替换成NaN，然后再进行删除或填充



fillna()
dropna()
'''

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('data/movie.csv')
# print(df)

# print(df.head(25))

# 1. 校验缺失值
# notnull：对每个单元格的元素值进行空值判断。如果为NaN，返回False；否则返回True
print(pd.notnull(df))

# isnull：对每个单元格的元素值进行空值判断。如果为NaN，返回True；否则返回False
print(pd.isnull(df))

# 是否所有的单元格都不为空。只要有一个单元格为NaN，就返回False；全部的单元格都不为NaN，才返回True
print(np.all(pd.notnull(df)))

# 只要有一个单元格不为NaN，就返回True；全部的单元格都为NaN，才返回False
print(np.any(pd.notnull(df)))

# 2. 删除缺失值
# 不修改原数据
new_data = df.dropna(axis=0)  # 以行为单位进行删除。如果行中只要有一个字段的值为NaN，那么该行就会被删除
print(new_data)

# 3. 空值填充
df1 = df.copy()

# 使用固定值对NaN值进行填充
# df1["Revenue (Millions)"].fillna(value=6666,inplace=True)

# 推荐：使用均值mean()均值、median()中位数对NaN值进行填充
df1["Revenue (Millions)"].fillna(value=df1["Revenue (Millions)"].mean(),inplace=True)

# 4. 异常值不是NaN。需要先替换成NaN，然后再进行删除或填充
df2 = pd.read_csv("data/breast-cancer-wisconsin.data",encoding="UTF-8")
df3 = df2.replace(to_replace="?",value=np.nan)
df3.dropna(axis=0)
print(df3)