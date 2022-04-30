# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def dfs(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            elif (nodep and not nodeq) or (nodeq and not nodep):
                return False
            
            leftNodes = dfs(nodep.left, nodeq.left)
            rightNodes = dfs(nodep.right, nodeq.right)
            equalNodes = nodep.val == nodeq.val and rightNodes and leftNodes
            return equalNodes
            
        return dfs(p, q)
        