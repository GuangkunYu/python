"""
1、将朋友的名字保存到列表中，命名为names，依次访问列表中的每个元素，将他们都打印出来
"""
names = ['张三', '李四', '王五', '赵六', '王八']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

"""
2、用1的列表，给每个人打印一条消息，每条消息都包含相同的问候语，抬头为每个朋友的姓名
"""
message = '，你好！'
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[3] + message)
print(names[4] + message)