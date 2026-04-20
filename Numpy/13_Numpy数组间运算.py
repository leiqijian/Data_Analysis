'''


'''

import numpy as np

arr = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])

# 普通运算
print(arr + 10)
print(arr - 2)
print(arr * 2)
print(arr / 2)

# 矩阵运算
# 前一个矩阵的列要等于后一个矩阵的行，结果为（前一个矩阵的行， 后一个矩阵的列）
# 数组 A: 形状 (2, 1)
A = np.array([[1],
              [4]])

# 数组 B: 形状 (1, 3)
B = np.array([[10, 20, 30]])

# 运算
# result = np.matmul(A,B)
result = A @ B

print(result)


# 广播机制
arr1 = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])   # 2 x 6
arr2 = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])  # 2 x 4
print(arr1 + arr2) #报错


# 1. 维度大小相等

# 数组 A: 形状 (2, 3)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# 数组 B: 形状 (2, 3)
B = np.array([[10, 20, 30],
              [40, 50, 60]])

# 运算
result = A + B

print("结果:\n", result)

# 2. 其中一个维度大小为 1
# 数组 A: 形状 (2, 3)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# 数组 B: 形状 (1, 3)
B = np.array([[10, 20, 30]])

# 运算
result = A + B

print("结果:\n", result)

# 3. 其中一个数组缺少该维度
# 创建一个形状: (3, 4)
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 创建一个形状: (1,4)
arr2 = np.array([10, 20, 30, 40])

# 进行加法运算
result = arr1 + arr2

print("运算结果:\n", result)




