#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


class Solution:
    def find_pairs(self, nums, target, start, end):
        b_c = []
        while start < end:
            left = nums[start]
            right = nums[end]
            if left + right == target:
                b_c.append((left, right))
                start += 1
                end -= 1
                while left == nums[start] and start < end:
                    start += 1
                while right == nums[end] and start < end:
                    end -= 1
            elif left + right < target:
                start += 1
                while left == nums[start] and start < end:
                    start += 1
            else:
                end -= 1
                while right == nums[end] and start < end:
                    end -= 1
        return b_c

    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        tried_combo = {}
        result = []
        end = len(sorted_nums)-1
        for i in range(end-1):
            a = sorted_nums[i]
            pairs = self.find_pairs(sorted_nums, -a, i+1, end)
            if pairs:
                for b, c in pairs:
                    triplet = [a, b, c]
                    set_triplet = frozenset(triplet)
                    if not set_triplet in tried_combo:
                        tried_combo[set_triplet] = 1
                        result.append(triplet)
        return result


Solution().threeSum([0, -1, 1])
