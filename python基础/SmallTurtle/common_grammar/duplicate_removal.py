# 需求：去掉列表中重复的元素
def duplicate_removal(lis):
    li = set(lis)
    return list(li)


if __name__ == "__main__":
    lis = [0, 1, 2, 3, 4, 5, 5, 3, 1]
    li = duplicate_removal(lis)
    print(li)
