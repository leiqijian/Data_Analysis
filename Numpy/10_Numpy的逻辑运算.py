'''


'''

import numpy as np

score = np.random.randint(40, 100, (10, 5))

test_score = score[6:, :]
print(test_score)

# 逻辑判断, 如果成绩大于60就标记为True 否则为False
print(test_score > 60)

# BOOL赋值, 将满足条件的设置为指定的值-布尔索引

test_score[test_score > 60] = 1
print(test_score)
