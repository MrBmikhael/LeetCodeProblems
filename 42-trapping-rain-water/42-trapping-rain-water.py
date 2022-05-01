class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        leftP = 0
        rightP = len(height)-1
        maxLeft = 0
        maxRight = 0
        totalWater = 0

        while (leftP != rightP):
            if height[leftP] <= height[rightP]:
                if height[leftP] > maxLeft:
                    maxLeft = height[leftP]
                else:
                    totalWater += maxLeft - height[leftP]
                leftP += 1
            else:
                if height[rightP] > maxRight:
                    maxRight = height[rightP]
                else:
                    totalWater += maxRight - height[rightP]
                rightP -= 1

        return totalWater