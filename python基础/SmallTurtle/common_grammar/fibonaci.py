# 斐波那契数列
# 1,1,2,3,5,8,13...
def fibonaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)


if __name__ == "__main__":
    num = int(input("请输入一个月份数："))
    result = fibonaci(num)
    print(f"{num} 个月之后兔子有：{result} 对")
