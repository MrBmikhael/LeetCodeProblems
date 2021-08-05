class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        largest = 0
        visited = {}
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] in visited:
                if visited[s[r]] >= l:
                    l = visited[s[r]]+1
            
            visited[s[r]] = r
            r += 1
            largest = max(r - l, largest)

        return largest
