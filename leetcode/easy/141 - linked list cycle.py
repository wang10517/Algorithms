# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        pt1 = head.next
        if pt1:
            pt2 = head.next.next
        else:
            return False
        
        while pt1 != pt2:
            if not pt1 or not pt2:
                return False 
            pt1 = pt1.next
            if pt2.next:
                pt2 = pt2.next.next
            else:
                return False
        return True