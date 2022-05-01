class Solution(object):
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]

        mid = self.binarySearch(nums,0, len(nums)-1, target)
        if mid == -1:
            return [-1,-1]

        start = mid
        end = mid

        while (start != -1):
            tempStart = start
            start = self.binarySearch(nums, 0, start-1, target)

        while (end != -1):
            tempEnd = end
            end = self.binarySearch(nums, end+1, len(nums)-1, target)
        
        return [tempStart, tempEnd]
