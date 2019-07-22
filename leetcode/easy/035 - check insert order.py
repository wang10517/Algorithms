# import math

# class Solution:
#     def searchInsert(self, nums, target) -> int:
#         if target in nums:
#             return nums.index(target)
#         
#         left, right = 0, len(nums)-1
#         ave = 0
#         while left < right:
#             ave = math.floor((right - left)/2+left)
#             if target < nums[ave]:
#                 if target > nums[ave - 1]
#                 right = ave -1 
#             else:
#                 left = ave -1

#         return left  
class Solution:
    def searchInsert(self, nums, target) -> int:
        if target in nums:
            return nums.index(target)
        for e in nums:
            if e == target or e > target:
                return nums.index(e)
        return len(nums)


sol = Solution()
print(sol.searchInsert([1,3,5,6],2))