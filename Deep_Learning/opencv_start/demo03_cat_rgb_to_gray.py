import cv2
# 把彩色图像转换为灰度图像，并查看灰度图像在计算机中又是怎样表示的

# 1、读取彩色猫图
rgb_cat = cv2.imread("images/cat.jpg")
print(rgb_cat)
print(rgb_cat.shape)

# 2、把彩色图片转换为灰度图片
gray_cat = cv2.cvtColor(rgb_cat, cv2.COLOR_BGR2GRAY)

# 3、查看灰度图片的像素内容
print(gray_cat)

# 4、查看灰度图片的维度信息
print(gray_cat.shape)

# 5、保存灰度图像
cv2.imwrite("images/gray_cat.jpg", gray_cat)
