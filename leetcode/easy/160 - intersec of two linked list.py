# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        preA = 0
        preB = 0
        while not headB or not headA:
            if headA is headB:
                return headA.val
            
            prevA = headA
            headA = headA.next
            prevB = headB
            headB = headB.next
            

    
        return None
        