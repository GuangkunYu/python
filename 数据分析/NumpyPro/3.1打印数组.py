import sys

import numpy as np

# 一维数组的打印
a = np.arange(6)
print(a)
print("----------------------------")

# 二维数组的打印
b = np.arange(12).reshape(4, 3)
print(b)
print("----------------------------")

# 三维数组的打印
c = np.arange(24).reshape(2, 3, 4)
print(c)
print("----------------------------")

# 超大数组的打印
d = np.arange(10000)
print(d)
e = np.arange(10000).reshape(100, 100)
print(e)

# 取消超大数组打印省略中心部分
f = np.arange(10000)
np.set_printoptions(threshold=sys.maxsize)
print(f)
