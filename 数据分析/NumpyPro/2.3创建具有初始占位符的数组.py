import numpy as np
from numpy import pi

# 创建具有初始占位符内容的数组
# 创建一个由0组成的数组
a = np.zeros((3, 4))
print(a)
print("-----------------------------")

# 创建一个由1组成的数组
b = np.ones((2, 3, 4), dtype=np.int16)
print(b)
print("-----------------------------")

# 创建一个初始内容随机的数组
c = np.empty((2, 3))
print(c)
print("-----------------------------")

# 创建一个由数字组成的数组
d = np.arange(10, 30, 5)
print(d)
e = np.arange(0, 2, 0.3)
print(e)
print("-----------------------------")

# arange与浮点参数一起使用时，用linspace函数
f = np.linspace(0, 2, 9)
print(f)
g = np.linspace(0, 2*pi, 100)
print(g)
h = np.sin(g)
print(h)

