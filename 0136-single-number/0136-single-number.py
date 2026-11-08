class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        num = 0

        for i in range(n):
            num = num ^ nums[i]

        return num