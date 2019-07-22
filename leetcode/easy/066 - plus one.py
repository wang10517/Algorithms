# anaylsis:
#     basically decimal digits
#     starting from the right to left, increment until 
#     reach from 9 to 0, then cascade that to the next digit


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits.copy()
        if len(digits) == 0:
            return [1]
        done = False
        for i in range(len(digits)-1, -1, -1):
            if done:
                break
            cur_digit = digits[i]
            if cur_digit < 9:
                result[i] = cur_digit + 1
                done = True
            else:
                result[i] = 0
        if not done:
            result.insert(0,1)
        return result

        

                