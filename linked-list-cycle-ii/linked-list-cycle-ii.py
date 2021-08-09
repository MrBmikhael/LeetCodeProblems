# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tort = head
        hare = head
        meetNode = None
        
        while tort and hare:
            tort = tort.next
            if hare.next == None:
                return None
            hare = hare.next.next
            if hare == tort:
                meetNode = hare
                break
                
        if meetNode == None:
            return None
        
        current = head
        while current != meetNode:
            current = current.next
            meetNode = meetNode.next
        return current