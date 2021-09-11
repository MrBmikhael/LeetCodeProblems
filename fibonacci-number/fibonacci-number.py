class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return n
        
        dpOne = 0
        dpTwo = 1
        
        for i in range(2, n+1):
            dpOne = dpOne + dpTwo
            dpTwo, dpOne = dpOne, dpTwo
        
        return dpTwo