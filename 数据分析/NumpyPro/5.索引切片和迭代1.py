import numpy as np

# 一维数组可以进行索引、切片和迭代操作，像列表一样
a = np.arange(10) ** 3
print(a)

# 索引
print(a[2])

# 切片
print(a[2:5])

a[:6:2] = -1000
print(a)

print(a[::-1])

# 迭代
for i in a:
    print(i ** (1 / 3.))
