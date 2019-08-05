import itertools

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = [] 
        for d1, d2 in itertools.zip_longest(num1[::-1],num2[::-1], fillvalue=0):
            total = carry + int(d1) + int(d2)
            digit = total % 10
            carry = (total - digit)//10 
            result.append(digit)
        
        if carry != 0:
            result.append(carry)
        
        return ''.join(result[::-1])
            