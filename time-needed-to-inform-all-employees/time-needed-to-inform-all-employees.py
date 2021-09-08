class Solution:
    
    def dfs(self, adjList: List[int], informTime: List[int], n: int):
        minutes = 0
        for i in adjList[n]:
            minutes = max(minutes, self.dfs(adjList, informTime, i) + informTime[n])
        return minutes
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = [[] for _ in range(n)]
        for i in range(n):
            if i != headID:
                adjList[manager[i]].append(i)

        minutes = self.dfs(adjList, informTime, headID)
        
        return minutes