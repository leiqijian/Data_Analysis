'''
1. np.linspace (start, stop, num, endpoint)
2. np.arange(start,stop, step, dtype)
3. np.logspace(start,stop, num)

'''

import numpy as np

a = np.linspace (1, 10, 10, dtype = int)

print(a)

b = np.arange(1, 10, 1)
print(b)

c = np.logspace(0,2, 3, base = 10)
print(c)



