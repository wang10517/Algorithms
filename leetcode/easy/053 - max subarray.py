import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = nums[0],0 
        for e in nums:
            cursum = max(e, cursum+e)
            maxsum = max(maxsum,cursum)
        return maxsum