'''
1. np.array(object, dtype) 新建一个，相当于深拷贝
2. np.asarray(a, dtype) 没有新建，引用指向同一片内存区域，相当于浅拷贝

'''

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = np.array(a, dtype = np.float32)

print(a)
print(b)

c = np.asarray(a)

print("-----")
# a[0, 1] = 99
a[0][1]  = 99
print(a)
print(b)
print(c)
