class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        distances = [float('inf')] * n
        adjList = [ list() for _ in range(n) ]
        distances[k-1] = 0
        heap = []
        heapq.heappush(heap, k-1)
        
        for i in range(len(times)):
            src = times[i][0]
            dst = times[i][1]
            weight = times[i][2]
            
            adjList[src-1].append([dst-1,weight])
        
        while heap:
            currentV = heapq.heappop(heap)
            adjV = adjList[currentV]
            for i in range(len(adjV)):
                vert = adjV[i][0]
                weight = adjV[i][1]
                if distances[currentV] + weight < distances[vert]:
                    distances[vert] = distances[currentV] + weight
                    heapq.heappush(heap, vert)

        output = max(distances)
        if output == float('inf'):
            return -1
        return output
    