'''
文件读取通过pandas
通过Dataframe对象进行文件写出
    read_csv()
    to_csv()
'''

import pandas as pd
import numpy as np

"""
读取
    参数解释：
        filepath_or_buffer：文件路径。相对、绝对路径都行。推荐相对
        sep：字段值之间的分隔符
        usecols：只读取文件中指定的列
"""
data = pd.read_csv(filepath_or_buffer= "data/stock_day.csv", sep = ",", usecols= ["open", "high", "low", "close"])
print(data.head())

'''
写出
    参数
        path_or_buf : 文件写出路径
        sep : 字段值之间的分隔符
        columns : 把dataframe中的那些列写入文件
        header : 是否在文件最上方显示字段名称
        index : 是否将索引列写入文件
        encoding : 编码格式
        mode : 模式，a ,w, r
'''

data.to_csv(
    path_or_buf = "data/temp.csv",
    sep=" ",
    columns=["open", "high", "low", "close"],
    header= False,
)

data.to_csv(
    path_or_buf = "data/temp2.csv",
    sep=" ",
    columns=["open", "high", "low", "close"],
    header= True,
    index= False,
    encoding= "utf-8",
    mode= "a", #a append追加， w，覆盖写入
)

