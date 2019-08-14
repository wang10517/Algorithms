#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
import math


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        sorted_nums = sorted(nums)
        result = math.inf
        dif = math.inf
        end = len(sorted_nums)-1
        for i in range(end-1):
            a = sorted_nums[i]
            min_dis, min_sum = self.find_pairs(sorted_nums, target-a, i+1, end)
            if min_dis < dif:
                dif = min_dis
                result = min_sum + a
                if min_dis == 0:
                    return result
        return result

    def find_pairs(self, nums, target, start, end):
        min_dis = math.inf
        min_sum = 0

        while start < end:
            left = nums[start]
            right = nums[end]
            if abs((left + right) - target) < min_dis:
                min_dis = abs((left + right) - target)
                min_sum = left + right
                if min_dis == 0:
                    return 0, min_sum
            if (left + right) < target:
                start += 1
                while left == nums[start] and start < end:
                    start += 1
            else:
                end -= 1
                while right == nums[end] and start < end:
                    end -= 1
        return min_dis, min_sum


Solution().threeSumClosest([-1, 2, 1, -4], 1)
