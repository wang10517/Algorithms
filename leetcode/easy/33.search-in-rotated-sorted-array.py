#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        pivot = 0
        for i in range(length - 1, 0, -1):
            if nums[i] < nums[i-1]:
                pivot = i
            

