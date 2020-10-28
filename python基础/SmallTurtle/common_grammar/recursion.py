"""
    递归求阶乘
        写一个求阶乘的的函数：
            正整数阶乘指从1乘以2乘以3乘以4一直乘到所要求的数
            例如：所给的数是5，则阶乘式是1×2×3×4×5，得到的积是120，所以120就是5的阶乘
"""


def recursion(x):
    if x == 1:
        return 1
    else:
        return x * recursion(x - 1)


if __name__ == "__main__":
    num = int(input("请输入一个整数："))
    result = recursion(num)
    print(f"{num} 的阶乘是：{result}")
