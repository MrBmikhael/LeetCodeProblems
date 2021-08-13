# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        tempList = list()
        
        while l1:
            tempList.append(l1.val)
            l1 = l1.next
        
        while l2:
            tempList.append(l2.val)
            l2 = l2.next
        
        tempList.sort()
        outputHead = ListNode(tempList[0])
        current = outputHead
        for i in range(1, len(tempList)):
            current.next = ListNode(tempList[i])
            current = current.next
        
        return outputHead