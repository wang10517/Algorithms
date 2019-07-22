# Analysis:
#     return false when there is a closing mark getting ahead of a openign mark
#     case 1: the char is opening mark:
#         push the corresponsing closing mark to the stack 
#     case 2: the char is closing mark
#         2.a: the stack has the closing mark:
#             valid if the closing stack is the first on the stack
#             false otherwise
#         2.b: the stack is absent of the closing mark:
#             invalid

                

class Solution:
    def isValid(self, s: str) -> bool:
        marks = {
            '{' : '}' ,
            '[' : ']' ,
            '(' : ')'
        }
        if not s:
            # Trivially true
            return True
        chars = [] 
        for e in s: 
            if e in marks.keys():
                chars.append(marks[e])
            else:
                if not chars:
                    return False
                elif chars[-1] == e:
                    chars.pop()
                else:
                    return False
        return not chars

        ## Pretty fast running time but has a considerable memory consumption


## Takeawya: 
# check if the subscriptable has an element at all before doing the subscription
# 
            
        
        