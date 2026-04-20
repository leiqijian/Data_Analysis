'''
1. np.linspace (start, stop, num, endpoint)
2. np.arange(start,stop, step, dtype)
3. np.logspace(start,stop, num)

'''

import numpy as np

a = np.linspace (1, 10, 10, dtype = int)

print(a) #[ 1  2  3  4  5  6  7  8  9 10]

b = np.arange(1, 10, 1) #[1 2 3 4 5 6 7 8 9]
print(b)

c = np.logspace(0,2, 3, base = 10)
print(c) # [  1.  10. 100.]



