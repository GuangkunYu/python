bingo = "小甲鱼是帅哥"
answer = input("请输入小甲鱼最想听得一句话：")

while True:
    if answer == bingo:
        break
    answer = input("抱歉，错了，请重新输入（回答正确才能退出游戏）：")

print("哎呦，帅哦~")
print("你真是小甲鱼肚子里的蛔虫啊~")