class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        destArr = [float("inf")] * n
        destArr[src] = 0
        
        for i in range(k+1):
            tmpDestArr = destArr[:]
            for s,d,p in flights:
                if destArr[s] != float("inf") and destArr[s] + p < tmpDestArr[d]:
                    tmpDestArr[d] = destArr[s] + p
            destArr = tmpDestArr
            
        if destArr[dst] == float("inf"):
            return -1
        else:
            return destArr[dst]
                
        