# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node, minVal, maxVal):
        if node.val <= minVal or node.val >= maxVal:
            return False
        if node.left:
            if not self.dfs(node.left, minVal, node.val):
                return False
        if node.right:
            if not self.dfs(node.right, node.val, maxVal):
                return False
        return True
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root, float('-inf'), float('inf'))