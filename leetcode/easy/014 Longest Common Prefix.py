## First implemented a brute force method
# running time O(mn) m- the number of strings, n- the number of charcters in the first string
# space complexity O(n) ?
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ls = ""
        if not strs:
            return "" 

        for index in range(len(strs[0])):
            cur = strs[0][index]
            for i in range(1,len(strs)):
                if index >= len(strs[i]) or strs[i][index] != cur:
                    return ls 
            ls = ls + cur

        return ls

# it seems that the memory usage of this algorithms is very heavy

# other better ways of doing the same thing?
        
# much better solution 
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs: return ""
#         if len(strs) == 1: return strs[0]
        
#         strs.sort()
#         p = ""
#         for x, y in zip(strs[0], strs[-1]):
#             if x == y: p+=x
#             else: break
#         return r

# the trick here is to use the alphabetic sorting of the strings
# so that only compare the first and last one would be enought since they are the 
# pair that are urtherest apart