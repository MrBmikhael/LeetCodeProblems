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
            if current.child:
                childNode = current.child
                newTail = current.next
                current.next = childNode
                childNode.prev = current
                while childNode.next:
                    childNode = childNode.next
                childNode.next = newTail
                if newTail:
                    newTail.prev = childNode
                current.child = None
            current = current.next
        
        return head
    