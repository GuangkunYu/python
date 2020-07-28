"""
字符串：一系列字符，用引号括起的，包括单引号和双引号。
"""
# title() 方法：以首字母大写的方式显示每个单词。
name = "ada lovelace"
print(name.title())

# upper() 方法：将字符串全部改为大写
print(name.upper())

# lower() 方法：将字符串全部改为小写
print(name.lower())

# 使用 + 拼接字符串，通过拼接可使用存储在变量中的信息来创建完整的信息
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +last_name
print(full_name)
print("hello, " + full_name.title() + "!")

# 使用制表符\t或换行符\n来添加空白
print("\tpython")
print("\npython\njava")

# rstrip() 方法：删除字符串末尾的空白，不改变变量值
favorite_language = "python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

# lstrip() 方法：删除字符串开头的空白
# strip() 方法：同时删除字符串两端的空白
favorite_language = " python "
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language)
print(favorite_language.strip())
