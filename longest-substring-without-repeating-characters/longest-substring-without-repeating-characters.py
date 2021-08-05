class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        largest = 0

        for j in range(len(s)):
            visited = set()
            for i in s[j:]:
                if i in visited:
                    break
                visited.add(i)
                largest = max(len(visited), largest)

        return largest