# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#         if not haystack:
#             return -1
#         if len(needle) > len(haystack):
#             return -1
       


#         for i in range(len(haystack)):
#             if haystack[i] == needle[0]:
#                 flag = True
#                 for j in range(1,len(needle)):
#                     if i+j >= len(haystack) or haystack[i+j] != needle[j]:
#                         flag = False
#                         break
#                 if flag: return i
        
#         return -1

# the above solution is too slow for marginal cases

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0
#         if not haystack:
#             return -1
#         if len(needle) > len(haystack):
#             return -1
       
#         count = 0
#         ledger = {} 

#         for i in range(len(haystack)):
#             if ledger:
#                 ledger_copy = ledger.copy()
#                 for key in ledger_copy:
#                     if haystack[key+ledger[key]] == needle[ledger[key]]:
#                         ledger[key] = ledger[key] + 1
#                         if ledger[key] == len(needle):
#                             return key
#                     else:
#                         ledger.pop(key)
                    
#             if haystack[i] == needle[0]:
#                 ledger[i] = 1
#                 if ledger[i] == len(needle):
#                     return i
#         return -1

# still a bit confused by this question, this solution is still too slow..
# why not just use the built in function?
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
        
            
            

        
