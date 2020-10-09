import numpy as np

# 数组操作的算术运算符会应用到元素级别

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

# 乘积操作
print(A * B)

# 矩阵乘积
print(A @ B)

print(A.dot(B))
