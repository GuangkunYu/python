"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
输入: 123
输出: 321
输入: -123
输出: -321
输入: 120
输出: 21
"""
class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        s = str(x)
        if x>=0:
            rev = reversed(s)
        else:
            p = s[1:]
            rev = reversed(p)
            rev =s[0] + result.join(rev)
        re = result.join(rev)
        return re


if __name__ == "__main__":
    s = Solution()
    num = 120
    print(s.reverse(num))