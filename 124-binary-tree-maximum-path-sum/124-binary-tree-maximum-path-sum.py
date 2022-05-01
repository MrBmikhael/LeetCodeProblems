# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        leftSubTree = self.dfs(node.left)
        rightSubTree = self.dfs(node.right)
        self.maxPath = max(self.maxPath, leftSubTree + rightSubTree + node.val, max(leftSubTree, rightSubTree) + node.val, node.val)
        return node.val + max(leftSubTree, rightSubTree, 0)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val
        self.dfs(root)
        return self.maxPath