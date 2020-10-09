import numpy as np

# 将一个数组拆分为几个较小的数组
a = np.floor(10*np.random.random((2, 12)))
print(a)
print("---------------------------------")

print(np.hsplit(a, 3))
print("---------------------------------")

print(np.hsplit(a, (3, 4)))

