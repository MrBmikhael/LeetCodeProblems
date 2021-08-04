class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compDict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in compDict:
                return [compDict[nums[i]], i]
            compDict[comp] = i
            