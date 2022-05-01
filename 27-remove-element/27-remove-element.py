class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        output = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[output], nums[i] = nums[i], nums[output]
                output += 1
        return output