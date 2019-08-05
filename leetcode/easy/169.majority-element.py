#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            if not num in ht:
                ht[num] = 1
            else:
                ht[num] += 1
                if ht[num] >= len(nums)/2:
                    return num
        if len(ht) == 1:
            return nums[0]
        return None
