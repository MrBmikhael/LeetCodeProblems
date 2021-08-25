class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        freshOranges = 0
        qRotten = list()
        qLen = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        minutes = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    qRotten.append([i,j])
                    qLen += 1
                    
        while qRotten:
            location = qRotten.pop(0)
            qLen -= 1

            for d in directions:
                newLocation = [location[0] + d[0], location[1] + d[1]]
                if newLocation[0] not in range(len(grid)) or newLocation[1] not in range(len(grid[0])):
                    continue
                if grid[newLocation[0]][newLocation[1]] == 1:
                    qRotten.append(newLocation)
                    freshOranges -= 1
                    grid[newLocation[0]][newLocation[1]] = 2

            if qLen == 0 and qRotten:
                minutes += 1
                qLen = len(qRotten)
        
        if freshOranges != 0:
            return -1
        
        return minutes