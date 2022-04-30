# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node):
        if node:
            leftTail = self.dfs(node.left)
            rightTail = self.dfs(node.right)
            
            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            if rightTail:
                return rightTail
            if leftTail:
                return leftTail
            return node
        else:
            return None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        