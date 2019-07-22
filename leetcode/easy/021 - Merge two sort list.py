# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Analysis:
#     essentially going through two linked list, first solution would just be 
#     creating two pointers to go through each linked list and keep comparing
#     until reach the end of either of the two lists
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## Assumption could perform in-place modification
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val > l2.val:
            result = ListNode(l2.val)
            l2 = l2.next
        else:
            result = ListNode(l1.val)
            l1 = l1.next
        end = result

        while not l1 is None and not l2 is None:
            if l1.val > l2.val:
                new_node = ListNode(l2.val)
                end.next = new_node
                end = end.next
                l2 = l2.next
            else:
                new_node = ListNode(l1.val)
                end.next = new_node
                end = end.next
                l1 = l1.next        
        if l1 is not None:
            end.next = l1
        elif l2 is not None:
            end.next = l2
        return result
    ## pretty fast in terms of both running timme and space complexity