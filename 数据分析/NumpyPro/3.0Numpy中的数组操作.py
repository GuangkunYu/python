import numpy as np

# 定义两个二维数组
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])

# 求a、b两个数组的和
array_sum = a + b
print("和：\n", array_sum)
print("----------------------------")

# 求a、b两个数组的差
array_difference = a - b
print("差：", array_difference)
print("----------------------------")

# 求a、b两个数组的积
array_product = a * b
print("积：", array_product)
print("----------------------------")

# 求a、b两个数组的商
array_quotient = a / b
print("商：", array_quotient)
print("----------------------------")

# 矩阵乘法
array_matrix_product = a.dot(b)
print("矩阵乘：",  array_matrix_product)
