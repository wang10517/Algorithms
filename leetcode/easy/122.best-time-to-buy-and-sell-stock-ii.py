#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                total += prices[idx] - prices[idx-1]
        return total
