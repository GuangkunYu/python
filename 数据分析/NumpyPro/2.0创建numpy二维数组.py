import numpy as np

# 创建一个2行3列的元素都为0的二维数组
my_2d_array0 = np.zeros((2, 3))
print(my_2d_array0)
print("---------------------")

# 创建一个2行4列的元素都为1的二位数组
my_2d_array1 = np.ones((2, 4))
print(my_2d_array1)
print("---------------------")

# 手动创建一个二维数组，并获取第一行第二列的数值
my_2d_array3 = np.array([[4, 5], [6, 1]])
print(my_2d_array3)
print(my_2d_array3[0][1])
print("---------------------")

# 输出二维数组的形状
print(my_2d_array3.shape)
print("---------------------")

# 输出二维数组第2列的所有元素
my_2d_array3_column_2 = my_2d_array3[:, 1]
print(my_2d_array3_column_2)
print("---------------------")
