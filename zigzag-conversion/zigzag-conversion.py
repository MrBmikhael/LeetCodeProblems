class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        line = 0
        outputStr = [""] * numRows
        direction = 1

        for i in range(len(s)):
            outputStr[line] += s[i]
            line += direction
            if line == numRows-1 or line == 0:
                direction *= -1
        
        return ''.join(outputStr)