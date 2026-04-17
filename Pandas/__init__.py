import pandas as pd
import numpy as np

score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
print(type(score))
print(type(score_df))
print(score)
print(score_df)


# 构造列索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造行索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

# 添加索引
data = pd.DataFrame(data = score, columns=subjects, index=stu) #传入一个ndarray对象，可以指定行列索引
data_df = pd.DataFrame(data = score_df) #传入一个df对象，如果行列索引对不上，会NAN

print(data)