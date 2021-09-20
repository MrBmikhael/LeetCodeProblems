class Solution:
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    def findCycle(self, grid, parentCell, cell, visited):
        visited[cell[0]][cell[1]] = True
        found = False
        for d in self.directions:
            nextCell = [cell[0] + d[0], cell[1] + d[1]]
            if nextCell[0] in range(len(grid)) and nextCell[1] in range(len(grid[0])) and nextCell != parentCell:
                if grid[cell[0]][cell[1]] == grid[nextCell[0]][nextCell[1]]:
                    if visited[nextCell[0]][nextCell[1]]:
                        return True
                    found = self.findCycle(grid, cell, nextCell, visited)
        return found
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = []
        for x in range(len(grid)):
            visited.append([False] * len(grid[0]))

        cycle = False
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if not visited[i][j]:
                    cycle = self.findCycle(grid, [], [i, j], visited)
                    if cycle:
                        return True
        return cycle
                        