class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        if not ' ' in s:
            return len(s)
        
        chars = s.split()
        for i in range(len(chars)-1, -1, -1):
            if chars[i].isalpha:
                return len(chars[i])
        return 0 