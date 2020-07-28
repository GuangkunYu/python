"""
1、整数，+ - * /
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)

# ** 表示乘方运算
print(3**2)
print(3**3)
print(10**6)

"""
2、浮点数：带小数点的数
"""
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.1 + 0.2)    # 结果包含的小数位数可能不确定

# str() 方法：将数字转换成字符串，避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)