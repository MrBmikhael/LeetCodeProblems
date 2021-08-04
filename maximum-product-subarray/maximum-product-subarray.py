import numpy as np

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lmin = lmax = gmax = nums[0]

        for i in nums[1:]:
            if i >= 0:
                lmin = min(i, lmin * i)
                lmax = max(i, lmax * i)
            else:
                lmin_tmp = min(i, lmax * i)
                lmax = max(i, lmin * i)
                lmin = lmin_tmp
            gmax = max(gmax, lmax)
        return gmax