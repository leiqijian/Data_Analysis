'''
索引：
    修改索引
'''


import pandas as pd
import numpy as np
from sympy import false

score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
# 构造列索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

data = pd.DataFrame(data = score, columns = subjects, index = stu)
print(data)
#  修改行列索引
stu = ["stu_" + str(i) for i in range(score_df.shape[0])]

data.index = stu
print(data)

# 但是不能单独修改一行索引
print(data.index[3])
# data.index[3] = '3'  error

# 重新设置索引 reset_index
# df = data.set_index('语文')
df = data.set_index(['语文', '数学'])
print(df)
df1 = data.reset_index(drop = True)
print(df1)
