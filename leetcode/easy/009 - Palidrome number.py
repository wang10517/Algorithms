# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Analysis:
#     1. convert the int to str 
#     2. keep it as int


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed, pali = self.reverse(x)
        if not pali:
            return False

        if reversed == x:
            return True
        else:
            return False
    
    def reverse(self, x: int) -> int:
        result = 0
        neg = False
        if x < 0:
            return None, False

        while x != 0:
            rem  = x % 10 
            result = result*10 +rem
            x = x // 10
        
        return result, True