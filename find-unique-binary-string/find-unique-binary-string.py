class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ints = set([int(s,2) for s in nums])
        maxInt = int(''.join(['1' for _ in nums]),2)
        
        for i in range(maxInt+1):
            if i not in ints:
                return "{0:b}".format(i).rjust(len(nums), "0")
        