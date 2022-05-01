class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adjList = [list() for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for i in range(len(prerequisites)):
            adjList[prerequisites[i][1]].append(prerequisites[i][0])
            degree[prerequisites[i][0]] += 1
        
        count = 0
        queue = []
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            d = queue.pop(0)
            count += 1
            for j in adjList[d]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
        
        return count == numCourses
