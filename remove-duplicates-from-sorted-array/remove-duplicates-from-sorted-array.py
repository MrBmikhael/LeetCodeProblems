class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[c] = nums[i]
                c += 1
        return c