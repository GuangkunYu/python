import os

# 当前工作文件夹   E:\GitHubCode\python\PyQt5\chapter11\02
print(os.getcwd())
print("-----------------------------")

# 相对路径
with open('message') as f:
    print(f.read())
with open('demo\\message') as file:
    print(file.read())
print('----------------------------')

# 绝对路径
print(os.path.abspath('message'))
# with open(r'E:\GitHubCode\python\PyQt5\chapter11\02\message') as f1:
#     print(f1.read())