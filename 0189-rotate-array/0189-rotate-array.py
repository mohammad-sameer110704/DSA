class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums2 = []

        for i in range(n - k, n):
            nums2.append(nums[i])

        for i in range(0, n - k):
            nums2.append(nums[i])

        nums[:] = nums2