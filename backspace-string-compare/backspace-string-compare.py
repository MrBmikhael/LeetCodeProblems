class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sString = []
        tString = []
        
        for i in s:
            if i != '#':
                sString.append(i)
            elif len(sString) > 0:
                sString.pop()
                
        
        for i in t:
            if i != '#':
                tString.append(i)
            elif len(tString) > 0:
                tString.pop()
                
        return sString == tString