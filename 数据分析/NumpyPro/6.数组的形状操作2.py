import numpy as np

a = np.floor(10 * np.random.random((2, 2)))
print(a)
print("----------------------------------")

b = np.floor(10 * np.random.random((2, 2)))
print(b)
print("----------------------------------")

# 将不同数组堆叠在一起    按行堆叠
print(np.vstack((a, b)))

# 按列堆叠  也可以用np.column_stack((a,b))
print(np.hstack((a, b)))

print("----------------------------------")

# 数组为一维数组时，上面两个函数的结果不同
c = np.array([4., 2.])
d = np.array([3., 8.])
print(np.column_stack((c, d)))
print(np.hstack((c, d)))
print("----------------------------------")

# 一维数组便二维
from numpy import newaxis
print(c[:, newaxis])
