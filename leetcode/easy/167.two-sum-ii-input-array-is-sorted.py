#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return None

        start, end = 0, len(numbers)-1

        while start < end:
            total = numbers[start] + numbers[end]
            if total > target:
                end -= 1
            elif total < target:
                start += 1
            else:
                return [start+1, end+1]
        return None
