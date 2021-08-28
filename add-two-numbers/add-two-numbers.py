# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1Num = 0
        l2Num = 0
        
        factor = 1
        while l1:
            l1Num += (factor*l1.val)
            factor *= 10
            l1 = l1.next
        
        factor = 1
        while l2:
            l2Num += (factor*l2.val)
            factor *= 10
            l2 = l2.next
        
        sumNum = l1Num + l2Num
        factor = 1
        sumHead = ListNode()
        current = sumHead
        
        if sumNum == 0:
            return ListNode()
        
        while sumNum != 0:
            val = (sumNum/factor) % 10
            sumNum -= (val*factor)
            current.next = ListNode(val)
            factor *= 10
            current = current.next

        return sumHead.next