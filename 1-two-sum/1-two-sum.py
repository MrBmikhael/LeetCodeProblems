class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in compDict:
                return [compDict[nums[i]], i]
            compDict[comp] = i