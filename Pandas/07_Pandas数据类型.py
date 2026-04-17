'''
查看数据类型
    df1.dtypes
    df1.info()

数据类型：
    datetime类型
    timedelta类型
    category类型
'''

import pandas as pd
import numpy as np
# 创建一个datetime类型的Series
dates = pd.to_datetime(['2024-09-01', '2024-09-02', '2024-09-03'])
print(dates)

# 计算两个日期之间的差值
start_date = pd.to_datetime('2024-09-01')
end_date = pd.to_datetime('2024-09-05')
delta = end_date - start_date
print(delta)

# 创建一个category类型的Series
categories = pd.Series(['apple', 'banana', 'apple', 'orange'], dtype='category')
print(categories)

