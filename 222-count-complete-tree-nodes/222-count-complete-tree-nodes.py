# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def nodeExists(self, root, index, height):
        left = 0
        right = (2**height)-1
        count = 0
        while count < height:
            midNode = math.ceil((left+right)/2.0)
            if index >= midNode:
                root = root.right
                left = midNode
            else:
                root = root.left
                right = midNode-1
            count += 1
        return root != None
        
        
    def leftHeight(self, node, count=0):
        if not node:
            return count
        return self.leftHeight(node.left, count+1)
    
    def rightHeight(self, node, count=0):
        if not node:
            return count
        return self.rightHeight(node.right, count+1)
    
    def binarySearch(self, root, height):
        left = 0
        right = (2**height)-1
        while left < right:
            mid = int(math.ceil((right+left)/2.0))
            if self.nodeExists(root, mid, height):
                left = mid
            else:
                right = mid-1
        return left
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        lHeight = self.leftHeight(root)
        
        if lHeight == 1:
            return 1
        
        rHeight = self.rightHeight(root)
        
        if lHeight == rHeight:
            return (2**lHeight)-1
        lastLevel = self.binarySearch(root, lHeight-1)
        return (2**(lHeight-1)) + lastLevel
            