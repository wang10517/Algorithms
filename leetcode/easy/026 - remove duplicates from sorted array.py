class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        mod = [prev]
        counter = 1
        for e in nums:
            if prev != e:
                counter = counter + 1
                prev = e
                mod.append(prev)
        nums[:counter] = mod
        return counter
    ## suprisingly fast but not memory efficient