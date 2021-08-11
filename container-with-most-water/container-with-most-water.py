class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        largest = 0
        
        while left < right:
            largest = max(min(height[left], height[right]) * (right-left), largest)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return largest