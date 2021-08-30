class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(set(strs)) == 1:
            return strs[0]
        
        out = ""
        index = 0
        while True:
            for i in strs:
                if i[:index] != out:
                    return i[:index-1]
            index += 1
            out = strs[0][:index]
