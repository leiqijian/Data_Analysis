'''
逻辑运算符：
    总结：
	1- 逻辑运算中不能使用单词and、or、not，必须使用对应的符号& | ~
    2- 每个比较运算符表达式必须使用小括号包起来
'''

import numpy as np
import pandas as pd

data = pd.read_csv("data/stock_day.csv")

print(data)
print(type(data))

# 筛选出open列大于22的数据，但是只会返回true 和 false的结果
# 2018-02-27     True
# 2018-02-26     True
# 2018-02-23     True
# 2018-02-22     True
# 2018-02-14    False
print((data["open"] > 22))

# 在筛选出true false结果上，外面包一层dataframe[]。可以获得对应的值
#              open   high  close
# 2018-02-27  23.53  25.88  24.16
# 2018-02-26  22.80  23.78  23.53
# 2018-02-23  22.88  23.37  22.82
# 2018-02-22  22.25  22.76  22.28
# 2018-02-07  22.69  23.11  21.80
print(data[data["open"] > 22])

# 与逻辑，每个比较运算表达式要用小括号包起来
print((data[
            (data["open"] > 22) & (data["close"] < 30)
            ]
      ))

# 或逻辑
print((data[(data["open"] > 22) | (data["close"] < 30)]))

# 非逻辑
print(data[ ~ (data["open"] > 22) ])

# query() 参数填字符串表达式，支持and or not
print(data.query("open>22 and close<=22 and low>=21"))

# isin() 可以指定值进行一个判断，从而进行筛选操作
print(data[
          data["open"].isin([22.69, 22.81, 22.91])
      ])