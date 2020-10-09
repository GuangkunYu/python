import numpy as np


# 二维数组每一个轴都有一个索引，这些索引以逗号分隔的元组给出
def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

print(b[2, 3])

# 切片
print(b[0:5, 1])

print(b[:, 1])

print(b[1:3, :])

# 当提供索引少于轴的数量时，缺失的索引被认为是完整的切片
print(b[-1])

print("-------------------")

# 迭代：多维数组的迭代是相对于第一个轴完成的
for row in b:
    print(row)

# 如果要对数组中的每个元素执行操作可以使用flat属性，该属性是数组的所有元素的迭代器
for element in b.flat:
    print(element)
