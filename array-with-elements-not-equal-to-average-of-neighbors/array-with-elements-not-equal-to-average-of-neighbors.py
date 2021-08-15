import math
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        r = len(nums)-1
        l = 0
        output = list()
        
        while l <= r:
            output.append(nums[l])
            l += 1
            
            if l <= r:
                output.append(nums[r])
                r -= 1
        return output