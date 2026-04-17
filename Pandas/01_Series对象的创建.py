import pandas as pd
import numpy as np

#自定义 series对象
# 索引个数要与元素个数保持一致
s1 = pd.Series([1.,2,3,4,5,6], index=['a','b','c','d','e','f'])
print(s1)

# 通过元组创建series对象
s2 = pd.Series((1, 2, 3, 4), index=['a','b','c','d'])
print(s2)

# 通过字典创建series对象，字典中的key会作为行索引，因为key值天生自带去重效果
s3 = pd.Series({'A':1,'B':2,'C':3,'D':4,'E':5,'F':6})
print(s3)


# 通过numpy创建series对象
s4 = pd.Series(np.array([1,2,3]))
print(s4)

s5 = np.arange(10)
print(s5)

s6 = np.arange(start=1,stop=10,step=1) # 左闭右开的区间
print(s6)


