import os

# 参数1：指定要进行重命名的文件   参数2：指定重命名后的文件
os.rename("message.txt", "text.txt")

# 也可以使用shutil模块的move方法对文件进行重命名
