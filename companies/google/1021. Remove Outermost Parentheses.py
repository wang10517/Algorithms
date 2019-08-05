class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        resultString = []
        openCounters = 0
        for char in S:
            if char == ')':
                openCounters -= 1 
            if openCounters != 0:
                resultString.append(char)
            if char == '(':
                openCounters += 1 
        return ''.join(resultString)
