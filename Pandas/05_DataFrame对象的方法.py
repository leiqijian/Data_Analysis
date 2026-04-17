'''
    head（）
    tail（）
    ...

'''

import pandas as pd
import numpy as np

score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
# 构造列索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

data = pd.DataFrame(data = score, columns = subjects, index = stu)
print(data.head()) #默认5行
print(data.tail(2))