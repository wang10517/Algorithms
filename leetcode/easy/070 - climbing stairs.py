# analysis:
#     think could be ahieved using recursion or dp
class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
            
    #     return self.climbStairs(n-1) + self.climbStairs(n-2) 
    # exceed the time limit 

    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(n+1)]

        for i in range(n+1):
            if i == 0:
                memo[i] = 0
            elif i == 1:
                memo[i] = 1
            elif i == 2:
                memo[i] = 2
            elif memo[i] == 0:
                memo[i] = memo[i-2] + memo[i-1]
        return memo[-1]        

## detailed solution here : https://leetcode.com/problems/climbing-stairs/solution/
