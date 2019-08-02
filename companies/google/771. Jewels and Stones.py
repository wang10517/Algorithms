class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ht = {}
        numJs = 0
        if not S :
            return 0 
        
        for char in S:
            if char in ht:
                ht[char] += 1
            else:
                ht[char] = 1
        
        for char in J:
            if char in ht:
                numJs += ht[char]
        return numJs
        