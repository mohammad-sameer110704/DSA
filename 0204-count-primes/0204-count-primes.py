class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # c = 0
        # for i in range(n):
        #     p = 0
        #     for j in range(1,i+1):
        #         if i % j == 0 :
        #             p += 1
        #     if p == 2 :
        #         c += 1
        #         p = 0
        #     else :
        #         p = 0
        # return c
        
class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1

        return sum(is_prime)

        
            

        