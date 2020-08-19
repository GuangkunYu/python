import cv2

# 使用OpenCV读取刚刚写入的图片，查看像素内容，查看形状或者说维度信息

# 1.通过OpenCV库读取图片
img_message = cv2.imread("images/demo013x2.png")

# 2.查看像素内容
print(img_message)

# 3.查看维度信息
print(img_message.shape)
