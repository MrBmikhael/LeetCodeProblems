"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        current = head
        
        while current:
            flatChildren = None
            if current.child:
                flatChildren = self.flatten(current.child)
                newTail = current.next
                current.next = flatChildren
                flatChildren.prev = current
                while flatChildren.next:
                    flatChildren = flatChildren.next
                flatChildren.next = newTail
                if newTail:
                    newTail.prev = flatChildren
                current.child = None
            current = current.next
        
        return head
    