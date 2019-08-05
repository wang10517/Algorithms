#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#


class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        if not n:
            return None

        while n > 0:
            quotient, remainder = divmod(n, 26)
            if remainder == 0:
                result.append('Z')
                quotient -= 1
            else:
                result.append(chr(ord('A') + remainder-1))
            n = quotient

        return ''.join(result[::-1])


def convertRadix(n, radix):
    result = []
    if not n:
        return 0

    while n:
        quotient, remainder = divmod(n, 26)
        result.append(str(remainder))
        n = quotient
    return ''.join(result[::-1])


print(convertRadix(52, 26))
