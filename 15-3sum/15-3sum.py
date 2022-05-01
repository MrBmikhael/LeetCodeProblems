class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            r = len(nums)-1
            l = i+1
            while l < r:
                thrSum = nums[i] + nums[l] + nums[r]
                if thrSum > 0:
                    r -= 1
                elif thrSum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output
