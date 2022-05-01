class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        row = 0
        outputStr = [""] * numRows
        direction = 1

        for i in range(len(s)):
            outputStr[row] += s[i]
            row += direction
            if row == numRows-1 or row == 0:
                direction *= -1
        
        return ''.join(outputStr)
