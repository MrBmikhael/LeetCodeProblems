class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        maxHeap = [ -int(n) for n in nums ]
        heapq.heapify(maxHeap)
        
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        
        return str(-maxHeap[0])
        