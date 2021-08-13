class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def convertToInt(s):
            out = 0
            for i in s:
                out *= 10
                out += (ord(i) - ord('0'))
            return out
        
        return str(convertToInt(num1)*convertToInt(num2))