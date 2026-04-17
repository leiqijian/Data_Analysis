'''
DataFrame对象的创建
'''
import pandas as pd
import numpy as np

# 1. 通过复杂容器数据进行创建dataframe

# 1.1 字典套列表
dict = {
    "date": ['2025-06-01', '2024-06-01', '2023-06-01'],
    "name": ['Tom', 'Jenny', 'Leimen'],
    "score": [90, 80, 70]
}
df = pd.DataFrame(dict)
print(df)


# 1.2 列表套元组
df2_data = [
    ('2021-08-21', 25, 81),
    ('2021-08-22', 26, 50),
    ('2021-08-23', 27, 56)
]
# data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame，
# index = 行索引， columns = 列索引, dtype =  , copy ,
df = pd.DataFrame(df2_data)
print(df)


# 1.3 使用numpy创建dataframe
data = np.random.randint(40, 100, (10, 5))
df = pd.DataFrame(data)
print(df)