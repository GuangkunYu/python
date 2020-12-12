flag = True
grades = []
while flag:
    grade = int(input("请输入成绩："))
    if 0 <= grade <= 100:
        grades.append(grade)
    elif grade == -1:
        avg = sum(grades) / len(grades)
        print(f"平均成绩：{avg}")
        flag = False

