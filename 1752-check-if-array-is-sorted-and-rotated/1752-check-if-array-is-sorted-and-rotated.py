class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        wrong = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                wrong += 1
        if wrong<=1:
            return True
        else:
            return False