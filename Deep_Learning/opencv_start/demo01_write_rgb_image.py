import numpy as np  # 科学运算库
import cv2  # 计算机视觉库

# 1.实例化代表图片的列表数据
image_data = [
    [[0, 0, 255], [0, 0, 255]],
    [[0, 255, 0], [0, 255, 0]],
    [[255, 0, 0], [255, 0, 0]],
]

# 2.把列表数据转换成numpy中的数组
image_array = np.array(image_data)

# 3.把转化好的数组对象写入到特定的文件中
cv2.imwrite("images/demo013x2.png", image_array)
