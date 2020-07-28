"""
1、将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单
"""
name = "Eric"
message = "Hello " + name + ", would you like to learn some Python today?"
print(message)

"""
2、将一个人名存储到一个变量中，在以小写、大写和首字母大写的方式显示人名
"""
name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

"""
3、打印一句名人的名言
"""
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

"""
4、将上句人名保存到变量，显示的消息保存到变量
"""
famous_person = "Albert Einstein"
message = ' once said, "A person who never made a mistake never tried anything new."'
print(famous_person + message)

"""
5、存储一个人名，并在开头结尾都有一些空白字符。
"""
name = " \t ericle \n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())