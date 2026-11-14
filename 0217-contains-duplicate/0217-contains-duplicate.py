class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()
        # for i in range (1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = dict[num]+1
            else:
                dict[num] = 1
        for value in dict.values():
            if value >= 2:
                return True
        return False