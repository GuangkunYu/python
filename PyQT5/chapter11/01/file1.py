# 打开文件
file = open("message.txt", 'w', encoding='utf-8')

# 写入文件内容
file.write('我不是一个伟大的程序员，我只是一个具有良好习惯的优秀程序员。\n')
file.write('靠代码行数来衡量开发进度，就像是凭重量来衡量飞机制造的进度。\n')
# 关闭文件
file.close()

# with语句打开文件
with open("text.txt", 'a', encoding='utf-8') as f:
    # 写入文件内容
    f.write('我不是一个伟大的程序员，我只是一个具有良好习惯的优秀程序员。\n')
    f.write('靠代码行数来衡量开发进度，就像是凭重量来衡量飞机制造的进度。\n')
    print(f.name)