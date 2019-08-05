#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#


# class Solution:
#     def addEle(self, ht, e):
#         if e in ht:
#             ht[e] += 1
#         else:
#             ht[e] = 1

#     def primeFactorization(self, n):
#         if n <= 1:
#             return {}
#         ht = {}
#         cur_prime = 2
#         while cur_prime**2 <= n:
#             if n % cur_prime == 0:
#                 self.addEle(ht, cur_prime)
#                 n = n // cur_prime
#             else:
#                 cur_prime += 1
#         self.addEle(ht, n)
#         return ht

#     def trailingZeroes(self, n: int) -> int:
#         num5, num2 = 0, 0
#         for i in range(1, n+1):
#             ht = self.primeFactorization(i)
#             if 2 in ht:
#                 num2 += ht[2]
#             if 5 in ht:
#                 num5 += ht[5]
#         return min(num2, num5)

class Solution:
    def trailingZeroes(self, n):
        r = 0
        while n >= 5:
            n //= 5
            r += n
        return r
