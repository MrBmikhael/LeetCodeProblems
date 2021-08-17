# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        output = []
        queue = [root]
        currentLevel = []
        level = 1
        count = 0
        
        while queue:
            node = queue.pop(0)
            currentLevel.append(node.val)            
            count += 1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if count == level:
                output.append(currentLevel)
                currentLevel = []
                count = 0
                level = len(queue)
            
        return output