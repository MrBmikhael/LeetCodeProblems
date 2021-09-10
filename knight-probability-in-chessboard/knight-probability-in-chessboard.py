class Solution(object):
    def knightProbability(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        directions = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
        dp = [ [ [0.0]*n for i in range(n)] for _ in range(k+1) ]
        dp[0][r][c] = 1.0
        
        for i in range(k):
            for j in range(n):
                for t in range(n):
                    total = 0.0
                    for d in directions:
                        newLocation = [j+d[0], t+d[1]]
                        lim = set(range(n))
                        if newLocation[0] in lim and newLocation[1] in lim:
                            dp[i+1][j][t] += dp[i][newLocation[0]][newLocation[1]]/8.0

        res = 0
        for i in range(n):
            for j in range(n):
                res += dp[k][i][j]
        return res
        