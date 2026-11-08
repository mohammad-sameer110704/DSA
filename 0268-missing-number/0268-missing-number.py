class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=0
        for num in nums:
            total=total+num
    
        s=(n*(n+1))/2
        nums=int(s)-total
        return nums