import numpy as np

# 定义一个包含15个元素的数组，成3行5列排列
a = np.arange(15).reshape(3, 5)

print(a)

# ndarray.ndim:数组的轴（维度）的个数
print(a.ndim)

# ndarray.shape: 数组的维度，这是一个整数的元组，表示每个维度中数组的大小
print(a.shape)

# ndarray.size：数组元素的总数。等于shape的元素的乘积
print(a.size)

# ndarray.dtype：描述数组中元素类型的对象
print(a.dtype)

# ndarray.itemsize: 数组中每个元素的字节大小。
print(a.itemsize)

# ndarray.data：该缓冲区包含数组的实际元素
print(a.data)

print(type(a))
