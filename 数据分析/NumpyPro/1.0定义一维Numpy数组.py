import numpy as np

# 定义一维numpy数组
my_array = np.array([1, 2, 3, 4, 5])

print(my_array)
print("---------------------------")

# 数组的形状
print(my_array.shape)
print("---------------------------")

# 通过索引打印numpy数组的值
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[3])
print(my_array[4])
print("---------------------------")

# 修改numpy数组的元素
my_array[0] = -1
print(my_array)
print("---------------------------")

# 创建一个长度为5、元素都为0的numpy数组
my_new_array = np.zeros(5)
print(my_new_array)
print("---------------------------")

# 创建一个长度为5、元素都为1的numpy数组
my_one_array = np.ones(5)
print(my_one_array)
print("---------------------------")

# 创建一个长度为5的随机值数组
my_random_array = np.random.random(5)
print(my_random_array)
print("---------------------------")
