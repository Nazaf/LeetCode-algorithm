class Solution(object):
    def twoSum(self, nums, target):
        data = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in data:
                data[num] = i
            else:
                return [data[n], i]
