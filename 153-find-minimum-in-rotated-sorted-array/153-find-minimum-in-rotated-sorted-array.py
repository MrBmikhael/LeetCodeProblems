class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        r = len(nums)-1
        l = 0
        
        if nums[l] < nums[r]:
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1