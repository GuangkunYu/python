"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
"""
class Solution:
    def twoSum(self, nums:list, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        

class Solution1:
    def twoSum(self, nums:list, target: int):
        dic = {}
        for key, value in enumerate(nums):
            print(key, value)
            if target-value in dic:
                return [dic[target-value], key]
            dic[value] = key
            print(dic)

if __name__ == "__main__":
    s = Solution1()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))