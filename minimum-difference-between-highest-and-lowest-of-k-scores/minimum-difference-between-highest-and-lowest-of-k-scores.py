class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        lowestDiff = float('inf')
        for i in range(0,len(nums)-k+1):
            elements = nums[i:i+k]
            highest = max(elements)
            lowest = min(elements)
            lowestDiff = min(lowestDiff, (highest-lowest))
            
        return lowestDiff