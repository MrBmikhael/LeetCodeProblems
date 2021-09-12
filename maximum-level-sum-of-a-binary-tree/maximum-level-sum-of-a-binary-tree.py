# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        elements = 1
        queue = [root]
        currentLevel = 1
        currentSum = 0
        maxSum = root.val
        maxLevel = 1
        nextElements = 0
        
        while queue:
            node = queue.pop(0)
            elements -= 1
            currentSum += node.val
            
            if node.right:
                queue.append(node.right)
                nextElements += 1
            if node.left:
                queue.append(node.left)
                nextElements += 1
            
            if elements == 0:
                if currentSum > maxSum:
                    maxSum = currentSum
                    maxLevel = currentLevel

                currentSum = 0
                currentLevel += 1
                elements = nextElements
                nextElements = 0

        return maxLevel