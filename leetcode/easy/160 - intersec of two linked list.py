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
        if headA is None or headB is None:
            return None

        appended_a, appended_b = False, False
        hdA, hdB = headA, headB

        while not headA is headB:
            if headA.next is None:
                if not appended_a:
                    headA = hdB
                    appended_a = True
                else:
                    return None
            else:
                headA = headA.next

            if headB.next is None:
                if not appended_b:
                    headB = hdA
                    appended_b = True
                else:
                    return None
            else:
                headB = headB.next

        return headA
