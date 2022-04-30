class Solution(object):
    def quickSelect(self, nums, l, r, k):
        pivot = nums[r]
        p = l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return self.quickSelect(nums, l, p-1, k)
        elif p < k:
            return self.quickSelect(nums, p+1, r, k)
        else:
            return nums[p]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = len(nums)-k
        return self.quickSelect(nums, 0, len(nums)-1, index)
