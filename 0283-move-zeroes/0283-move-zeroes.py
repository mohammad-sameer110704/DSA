class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for k in range(n):
            if nums[k]==0:
                j=k
                break
        j=k
        for i in range(j+1,n):
            if nums[j]!=nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
                j=j+1
        return nums
