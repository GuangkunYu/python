import numpy as np

# 数组操作的算术运算符会应用到元素级别

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)

# 减法操作
c = a - b

print(c)

# 乘方操作
print(b ** 2)

# sin操作
print(10 * np.sin(a))

# 比较大小操作
print(a < 35)
