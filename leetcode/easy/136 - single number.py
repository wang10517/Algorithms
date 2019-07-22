class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for e in nums:
            if not e in s:
                s.add(e)
            else:
                s.remove(e)
        return s.pop()