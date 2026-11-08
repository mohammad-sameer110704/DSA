class Solution(object):
    def subarraySum(self, nums, k):
        prefix = 0
        c = 0

        dic = {0: 1}

        for i in range(len(nums)):
            prefix = prefix + nums[i]

            if prefix - k in dic:
                c = c + dic[prefix - k]

            if prefix in dic:
                dic[prefix] = dic[prefix] + 1
            else:
                dic[prefix] = 1

        return c




        