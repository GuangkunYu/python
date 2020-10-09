import numpy as np

a = np.floor(10 * np.random.random((3, 4)))
print(a)

print(a.shape)

# 更改数组的形状
# 以下三个命令都返回一个修改后的数组，但不会更改原始数组
print(a.ravel())    # 降维 C风格
print(a.reshape(6, 2))      # 改变数组的形状，返回带有修改形状的参数

print(a.T)      # 数组倒置

print(a)
# reshape方法中如果将size指定为-1，则会自动计算其他的size大小
print(a.reshape(3,-1))

# resize方法会修改数组本身
a.resize((2,6))
print(a)