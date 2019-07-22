# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

## other assumptions:
    # the array is not sorted

## Analysis: 
## 1. Could be solved by brute force easily with running time of O(N^2)
## 2. To bring down the running time 
##      one solution is to loop through the array and get target - list[i], set it in hasshset for later lookup, if found in looping =>true
# this solution has O(N) running time and O(N) for memory space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            diff = target - list[i]
            if diff in lookup:
                return [i,lookup[diff]]
            else: 
                lookup[list[i]] = i
        
## seems to be the optimal solution