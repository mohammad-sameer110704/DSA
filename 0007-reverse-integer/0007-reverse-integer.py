class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            rev=0
            while(x>0):
                rem=x%10
                rev=rev*10+rem
                x=x/10
            num = rev 
        else:
            x=x*(-1)
            rev=0
            while(x>0):
                rem=x%10
                rev=rev*10+rem
                x=x/10
            num = -rev
        if -2**31 <= num <= 2**31 -1:
            return num
        else :
            return 0