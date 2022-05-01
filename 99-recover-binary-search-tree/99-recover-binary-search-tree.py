# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        def dfs(node):
            if node:
                dfs(node.left)
                nodes.append(node)
                dfs(node.right)
        
        dfs(root)
        switchedNodes = []
        for i, node  in enumerate(sorted(nodes, key=lambda n:n.val)):
            if nodes[i].val != node.val:
                switchedNodes.append(i)
        
        nodes[switchedNodes[0]].val, nodes[switchedNodes[1]].val = nodes[switchedNodes[1]].val, nodes[switchedNodes[0]].val
        