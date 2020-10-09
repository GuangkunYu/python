import numpy as np

# 数组操作的算术运算符会应用到元素级别

# 计算数组中所有元素的总和
a = np.random.random((2, 3))
print(a)

# 数组所有元素的和
print(a.sum())

# 数组的最小值
print(a.min())

# 数组的最大值
print(a.max())
print("--------------")

# 通过指定axis参数，可以指定轴操作
b = np.arange(12).reshape(3, 4)
print(b)

# 计算数组每一列的和 axis=0:表示列
print(b.sum(axis=0))

# 查找没一行的最小值 axis=1：表示行
print(b.min(axis=1))

# 计算每一行的累和
print(b.cumsum(axis=1))
