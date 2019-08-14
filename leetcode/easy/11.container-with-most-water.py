#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start, end = 0, len(height)-1
        while start < end:
            curArea = (end - start)*min(height[start], height[end])
            maxArea = max(curArea, maxArea)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxArea
