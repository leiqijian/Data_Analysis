'''


'''

import numpy as np
from sqlalchemy.engine import result

score = np.random.randint(40, 100, (10, 5))

# 判断前两名同学的成绩[0:2, :]是否全及格

print(np.all(score[0:2, :] > 60 ))

# 判断前两名同学的成绩[0:2, :]是否有大于90分的

print(np.any(score[0:2, :] > 90 ))

# 判断前四名学生,前四门课程中，成绩中大于60的置为1，否则为0

temp = score[:4, :4]

np.where(temp > 60, 1, 0)

# 判断前四名学生,前四门课程中，成绩中大于60且小于90的换为1，否则为0
# result = np.where( (temp > 60) & (temp < 90), 1, 0 )
result_and = np.where(np.logical_and(temp > 60 , temp < 90), 1, 0 )
print(result)

# 判断前四名学生,前四门课程中，成绩中大于90或小于60的换为1，否则为0

result_or = np.where(np.logical_or(temp > 90, temp < 60), 1, 0)
