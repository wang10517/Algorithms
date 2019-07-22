# analysis:
#     perform simple binary adder:
#         1 + 1 = 0 + increment
#         1 + 0 = 1
#         0 + 0 = 0
#     special case:
#         unequal length
#         insertion of new digit
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a is None or not a:
            return b
        if b is None or not b:
            return a
        res = ""
        shorter = ""
        longer = ""
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        carry = 0
        for i in range(-1,-len(shorter)-1, -1):
            curd, carry = self.digit_adder(shorter[i], longer[i], carry)
            res = curd + res
        
        if carry == 1:
            res = self.addBinary(longer[:len(longer) - len(shorter)], '1')+res
        else:
            res = longer[:len(longer) - len(shorter)] + res
        return res

    def digit_adder(self,s1, s2,carry):
        su = int(s1)+int(s2) + int(carry)
        if su <= 1:
            return str(su), 0
        elif su == 2:
            return '0', 1
        else:
            return '1', 1

print(Solution().addBinary("100", "110010"))
        

