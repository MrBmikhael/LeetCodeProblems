# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tempList = []
        
        for l in lists:
            while l:
                tempList.append(l.val)
                l = l.next
        
        if not tempList:
            return None
        
        tempList.sort()
        outputHead = ListNode(tempList[0])
        current = outputHead
        for i in range(1, len(tempList)):
            current.next = ListNode(tempList[i])
            current = current.next
        return outputHead