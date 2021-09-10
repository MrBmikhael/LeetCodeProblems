class Solution(object):
    def minCost(self, cost, i, dp):
        if i == 0 or i == 1:
            return cost[i]
        elif i < 0:
            return 0
        if dp[i] != None:
            return dp[i]
        dp[i] = cost[i] + min(self.minCost(cost, i-1, dp), self.minCost(cost, i-2, dp))
        return dp[i]
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [None] * n
        return min(self.minCost(cost, n-1, dp), self.minCost(cost, n-2, dp))
        
        