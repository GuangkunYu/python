import numpy as np

a = np.arange(12) ** 2
print(a)
print("--------------------")

# 使用索引数组进行索引查询
i = np.array([1, 1, 3, 8, 5])
print(a[i])

j = np.array([[3, 4], [9, 7]])
print(a[j])
print("--------------------")

