class Solution:
    def findDisappearedNumbers(self, nums: List[int ]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i+1)
        return res