import math
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        mid = int(math.ceil(len(nums) / 2))
        numsA = nums[:mid]
        numsB = nums[mid:]
        output = list()
        
        for i in range(len(nums)):
            if i % 2 == 0:
                output.append(numsB.pop())
            else:
                output.append(numsA.pop())
        return output