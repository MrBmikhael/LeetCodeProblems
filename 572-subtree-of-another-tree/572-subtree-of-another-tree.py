# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root:
            if root.val == subRoot.val:
                if self.isIdentical(root,subRoot):
                    return True
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isIdentical(self,root,subRoot):
        if (root == None and subRoot != None) or (root != None and subRoot == None):
            return False
        if root == None and subRoot == None:
            return True
        return root.val == subRoot.val and self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
    