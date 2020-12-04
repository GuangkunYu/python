with open('text.txt', 'r', encoding='utf-8') as file:

    # 读取指定个数字符
    print(file.read(5))
    # print(file.read())
    print("-----------------------")

    # 读取一行
    file.seek(9)
    print(file.readline())
    print('----------------------')

    #　读取所有行
    print(file.readlines())
