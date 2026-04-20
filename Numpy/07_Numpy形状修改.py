'''


'''

import numpy as np

# 创建一个 1x9 的数组
arr_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

reshaped_arr = arr_1.reshape(3, 3)
print(reshaped_arr)


# 创建一个 1x9 的数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55])

# 调整数组的大小为 2x5
resized_arr = np.resize(arr, (2, 5))
print(resized_arr)

transposed_arr = resized_arr.T
print(transposed_arr)