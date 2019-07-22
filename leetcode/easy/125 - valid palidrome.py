class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = s.split()
        if not chars:
            return True

        return chars == chars[::-1]
            