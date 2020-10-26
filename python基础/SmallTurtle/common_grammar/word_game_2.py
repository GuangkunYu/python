import random

print("-------------------我爱鱼C工作室-------------------")
screat = random.randint(1, 10)
temp = input("不妨猜一下小甲鱼现在心里想的数字是哪个：")
guess = int(temp)
flag = True
while flag:
    if guess == screat:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        flag = False
    else:
        if guess > screat:
            print("哥，大了，大了~~~")
        else:
            print("嘿，小了，小了~~~")
        temp = input("哎呀，猜错了，请重新输入吧：")
        guess = int(temp)

print("游戏结束，不玩了^_^")
