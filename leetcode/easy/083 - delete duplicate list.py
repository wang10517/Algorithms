# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        result = ListNode(head.val)
        cur = result
        temp = head
        while temp.next != None:
            temp = temp.next
            if temp.val != cur.val:
                cur.next = ListNode(temp.val)
                cur = cur.next
        return result