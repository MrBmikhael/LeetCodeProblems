# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, level=0, output=[]):
        if not node:
            return output
        
        if level >= len(output):
            output.append(node.val)
            
        if node.right:
            self.dfs(node.right, level+1, output)
            
        if node.left:
            self.dfs(node.left, level+1, output)
            
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, 0, result)
        return result