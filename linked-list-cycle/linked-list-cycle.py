# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd's tortoise and Hare Algo
        
        if head == None:
            return None
        
        tort = head
        hare = head
        
        while True:
            tort = tort.next
            hare = hare.next
            if hare == None or hare.next == None:
                return False
            hare = hare.next
            if hare == tort:
                return True
