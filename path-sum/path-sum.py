# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(node, currentSum):
            if not node:
                return False
            newSum = currentSum + node.val
            if newSum == targetSum and not node.left and not node.right:
                return True
            return dfs(node.left, newSum) or dfs(node.right, newSum)
        
        return dfs(root, 0)