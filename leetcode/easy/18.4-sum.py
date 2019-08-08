#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        results = []
        self.findSumWithN(nums, target, 4, 0, len(nums)-1, [], results)
        return results

    def findSumWithN(self, nums, target, N, start, end, result, results):
        if len(nums) < N or N < 2 or target < nums[start]*N or target > nums[end]*N:
            return

        if N == 2:
            while start < end:
                left = nums[start]
                right = nums[end]
                total = left + right
                if total == target:
                    results.append(result + [left, right])
                    start += 1
                    end -= 1
                    while nums[start] == left and start < end:
                        start += 1
                    while nums[end] == right and start < end:
                        end -= 1
                elif total < target:
                    start += 1
                    while nums[start] == left and start < end:
                        start += 1
                else:
                    end -= 1
                    while nums[end] == right and start < end:
                        end -= 1
        else:
            for i in range(start, end-N+2):
                if i == start or (nums[i] != nums[i-1]):
                    self.findSumWithN(
                        nums, target - nums[i], N - 1, i+1, end, result + [nums[i]], results)
        return


Solution().fourSum([0, 2, 2, 2, 10, -3, -9, 2, -10, -4, -9, -2, 2, 8, 7], 6)
