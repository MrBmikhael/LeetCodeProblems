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
        dpOne = [ [0.0]*n for i in range(n) ]
        dpTwo = [ [0.0]*n for i in range(n) ]
        dpOne[r][c] = 1.0
        
        for i in range(k):
            for j in range(n):
                for t in range(n):
                    total = 0.0
                    for d in directions:
                        newLocation = [j+d[0], t+d[1]]
                        lim = set(range(n))
                        if newLocation[0] in lim and newLocation[1] in lim:
                            dpTwo[j][t] += dpOne[newLocation[0]][newLocation[1]]/8.0
            dpOne = dpTwo
            dpTwo = [ [0.0]*n for i in range(n) ]

        res = 0
        for i in range(n):
            for j in range(n):
                res += dpOne[i][j]
        return res
        