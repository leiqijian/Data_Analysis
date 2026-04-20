'''
np.unique(): 把数据拆散然后删除重复项

'''

import numpy as np

temp = np.array([[1, 2, 3, 4],[3, 4, 5, 6]])

result = np.unique(temp)

print(result)