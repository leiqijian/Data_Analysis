'''
生成 0 和 1 的数组
    - np.ones(shape, dtype)
    - np.ones_like(a dtype)
    - np.zeros(shape, dtype
    - np.zeros_like(b, dtype)
    - np.empty(shape, dtype)

'''

import numpy as np

a = np.ones([4,8])

print(a)

b = np.zeros_like(a)
print(b)