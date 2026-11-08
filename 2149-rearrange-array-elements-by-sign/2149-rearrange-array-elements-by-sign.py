class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numms=[]
        pp=0
        np=1
        for num in nums:
            if num>0:
                numms.insert(pp,num)
                pp +=2
            else:
                numms.insert(np,num)
                np +=2     
        return numms

            

        