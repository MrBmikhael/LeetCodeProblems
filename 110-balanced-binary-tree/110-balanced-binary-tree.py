# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(node):
            if not node:
                return [True, 0]
            
            leftSubTree = dfs(node.left)
            rightSubTree = dfs(node.right)
            
            balanced = leftSubTree[0] and rightSubTree[0] and abs(leftSubTree[1] - rightSubTree[1]) <= 1
            
            return [balanced, 1 + max(leftSubTree[1], rightSubTree[1])]
        
        return dfs(root)[0]
        