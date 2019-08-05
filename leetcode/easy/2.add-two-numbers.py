#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        carry , cur_digit = divmod(l1.val + l2.val, 10)
        result = ListNode(cur_digit)
        rHead = result
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            carry , cur_digit = divmod(l1.val + l2.val + carry, 10)
            result.next = ListNode(cur_digit)
            result = result.next
        while l1.next:
            l1 = l1.next
            carry , cur_digit = divmod(l1.val + carry, 10)
            result.next = ListNode(cur_digit)
            result = result.next
        while l2.next:
            l2 = l2.next
            carry , cur_digit = divmod(l2.val + carry, 10)
            result.next = ListNode(cur_digit)
            result = result.next
        if carry:
            result.next = ListNode(carry)
        return rHead



        

