class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        repl = []        
        if not nums:
            return 0

        for e in nums:
            if e != val:
                repl.append(e)
        
        nums[:] = repl
        return len(repl)
                