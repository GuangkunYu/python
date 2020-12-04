import os

# 创建一级文件夹
if not os.path.exists("demo2"):
    os.mkdir("demo2")
    print("文件夹创建成功")
else:
    print("文件夹已经存在")


# 创建多级文件夹
os.makedirs(r"demo3\\demo4\\demo5")