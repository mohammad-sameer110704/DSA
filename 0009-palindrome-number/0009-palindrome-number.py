class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        org=x
        rev=0
        while(x>0):
            n=x%10
            rev = rev*10+n
            x = x//10
        if org == rev:
            return True
        return False
        