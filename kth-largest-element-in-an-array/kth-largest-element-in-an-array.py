class Solution(object):
    
    def partition(self, nums, left, right):
        pivot = nums[right]
        partIndex = left
        j = left
        
        while j < right:
            if nums[j] < pivot:
                nums[partIndex], nums[j] = nums[j], nums[partIndex]
                partIndex += 1
            j += 1
        nums[partIndex], nums[right] = nums[right], nums[partIndex]
        return partIndex
    
    def quickSelect(self, nums, left, right, k):
        if left < right:
            partIndex = self.partition(nums, left, right)
            if partIndex == k:
                return nums[k]
            elif k < partIndex:
                return self.quickSelect(nums, left, partIndex-1, k)
            else:
                return self.quickSelect(nums, partIndex+1, right, k)
        else:
            return nums[left]

        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = len(nums)-k
        return self.quickSelect(nums, 0, len(nums)-1, index)
        