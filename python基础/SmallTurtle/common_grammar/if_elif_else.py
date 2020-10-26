score = int(input("请输入成绩："))
if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 70:
    print("C")
elif 70 > score >= 60:
    print("D")
elif 60 > score >= 0:
    print("E")
else:
    print("输入错误")
