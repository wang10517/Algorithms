# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Analysis：
#     loop through each digit and append that into a new number
#     cases:
#         negative number 
#         overflow problem
#     runningtime O(n) for n the number of digits in a number (log10(x))

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        neg = False
        if x < 0:
            neg = True
            x = x*(-1)

        while x != 0:
            rem  = x % 10 
            result = result*10 +rem
            x = x // 10
        
        if neg:
            result = result*(-1)
        
        if result > 2**31 -1 or result < -2**31:
            return 0
        else:
            return result
            
if __name__ == '__main__':
    x = input()
    sol = Solution()
    print(sol.reverse(int(x)))