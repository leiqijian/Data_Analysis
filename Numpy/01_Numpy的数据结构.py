'''
ndarray
    属性：
        ndarray.shape
        ndarray.ndim
        ndarray.size
        ndarray.itemsize
        ndarray.dtype

    形状：
        ndarray.shape

    类型：
        ndarray.dtype
'''

import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.shape) #(4,) 4行一列
print(b.shape) #(2, 3) 2行3列

d = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float64)
print(d)

e = np.array(['python', 'tensorflow', 'scikit-learn', 'numpy'], dtype= 'U12')
print(e.dtype)

arr = np.array(['python', 'tensorflow', 'scikit-learn', 'numpy'], dtype = np.str_)
print(arr.dtype)


