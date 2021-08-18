class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue = list()
        visited = list()
        islands = 0
        directionsArr = [[-1,0],[0,1],[0,-1],[1,0]]
        
        for i in grid:
            visited.append([False] * len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    if grid[i][j] == "1":
                        islands += 1
                        queue.append([i,j])
                        while queue:
                            location = queue.pop(0)
                            visited[i][j] = True
                            for d in directionsArr:
                                newLoc = [d[0]+location[0], d[1]+location[1]]
                                if newLoc[0] >= 0 and newLoc[0] < len(grid) and newLoc[1] >= 0 and newLoc[1] < len(grid[0]):
                                    if grid[newLoc[0]][newLoc[1]] == "1" and visited[newLoc[0]][newLoc[1]] == False:
                                        queue.append(newLoc)
                                        visited[newLoc[0]][newLoc[1]] = True
        
        return islands