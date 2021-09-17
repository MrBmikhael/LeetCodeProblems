# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, targetSum, currentPath, paths):
        if not node:
            return
        
        currentPath.append(node.val)
        if node.left == None and node.right == None:
            if node.val == targetSum:
                paths.append(currentPath)
            else:
                currentPath.pop()
            return
        
        self.dfs(node.left, targetSum-node.val, currentPath[:], paths)
        self.dfs(node.right, targetSum-node.val, currentPath[:], paths)
        
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []
        self.dfs(root, targetSum, [], paths)
        return paths
        