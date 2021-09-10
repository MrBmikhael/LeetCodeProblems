class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [cost[0], cost[1]]
        n = len(cost)

        for i in range(2,n):
            dp[i%2] = cost[i] + min(dp[(i%2)-1], dp[(i%2)-2])
        
        return min(dp)
        
        