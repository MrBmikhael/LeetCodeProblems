class Solution(object):
    directions = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    def recurse(self, n,k,r,c,dp):
        if r < 0 or r >= n or c < 0 or c>= n:
            return 0
        if k == 0:
            return 1
        if dp[k][r][c]:
            return dp[k][r][c]
        res = 0
        for i in self.directions:
            res += self.recurse(n,k-1,r+i[0],c+i[1],dp)/8.0
        dp[k][r][c] = res
        return res
    
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        
        dp = [ [ [None]*n for i in range(n)] for _ in range(k+1) ]
        return self.recurse(n,k,row,column,dp)
        
        