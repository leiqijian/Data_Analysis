'''
属性：
    1. 行索引 dataFrame.index
    2. 列索引 dataFrame.columns
    3. 形状 dataFrame.shape
    4. 数据值 dataFrame.values
    5. 转置 dataFrame.T, 行转列，列转行
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
print(data)

print(f"shape: {data.shape}")
print(f"index: {data.index}")
print(f"columns: {data.columns}")
print(f"values: {data.values}")
print(f"转置T: {data.T}")