'''
ndarray.astype(type) : 返回修改了类型之后的数组
ndarray.tobytes() : 构造包含数组中原始数据字节的Python字节

'''

import numpy as np

# 创建一个浮点数类型的数组
arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

# 使用 .astype(np.int32) 将数组的元素类型转换为 int32
arr_int32 = arr.astype(np.int32)
print(arr_int32)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[12, 3, 34], [5, 6, 7]]])
print(type(arr.tobytes()))
print(arr.tobytes())