# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node:
                leftSub = dfs(node.left)
                rightSub = dfs(node.right)

                if leftSub and rightSub:
                    return node
                elif (leftSub or rightSub) and (node in [p,q]):
                    return node
                elif node in [p,q]:
                    return node

                return leftSub or rightSub

        return dfs(root)