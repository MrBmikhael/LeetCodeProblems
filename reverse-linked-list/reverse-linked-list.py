# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        current = head
        
        while current:
            values.append(current.val)
            current = current.next
            
        current = head
        while values:
            current.val = values.pop()
            current = current.next
            
        return head
            