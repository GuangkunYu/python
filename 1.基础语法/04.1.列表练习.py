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

"""
3、创建列表，邀人共进晚餐
"""
names = ['张三', '李四', '王五']
one = names.pop()
two = names.pop()
three = names.pop()
message = '请与我共进晚餐'
print(one + message)
print(two + message)
print(three + message)

"""
4、有一位不能参加，需要换人
"""
names = ['张三', '李四', '王五']
print(names[1] + '不能赴约')
names[1] = '赵六'
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)

"""
5、找到一个更大的餐桌，继续邀请人
"""
print('找到一个更大的餐桌')
names.insert(0, '田七')
print(names)
names.insert(2, '王八')
print(names)
names.append('啾啾')
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[3] + message)
print(names[4] + message)
print(names[5] + message)

"""
6、无法及时抵达，只能邀请两位人
"""
print('只能来两位了')
one = names.pop()
print(one + '抱歉')
two = names.pop()
print(two + '抱歉')
three = names.pop()
print(three + '抱歉')
four = names.pop()
print(four + '抱歉')
print(names)
print(names[0] + message)
print(names[1] + message)

del names[0]
print(names)
del names[1]
print(names)
print('\n')