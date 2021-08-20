class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            r = x % 10
            l = x // div
            if r != l:
                return False
            x = (x % div) // 10
            div = div / 100
            
        return True