'''
dataframe的json读写
    read_json()
    to_json()
'''

import pandas as pd
from sympy import false

"""
    参数解释：
        path_or_buf：文件路径
        orient：JSON格式。推荐使用records，那么JSON的格式就是键值对的形式
        lines：数据中每一行试一个单独的JSON
"""
# 读取Json文件
data = pd.read_json(path_or_buf="data/test.json", orient="records", typ='frame', lines=false)

print(data)

# 以JSON格式写出到文件
'''
DataFrame.to_json(path_or_buf=None,orient=None,lines=False)
    - path_or_buf: 文件地址
    - orient: 存储的json形式，{‘split’,’records’,’index’,’columns’,’values’} 推荐使用records
    - lines: 一个对象存储为一行 推荐使用True
'''
data.to_json(path_or_buf="data/copy1_json.json",orient="records",lines=True)
