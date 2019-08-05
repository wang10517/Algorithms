# assume all char in string is lower cased letters


def isPalindromePermu(string):
    bitVector = 0
    for char in string:
        shift = (1 << (ord(char)-ord('a')))
        if bitVector & shift == 0:
            bitVector = bitVector | shift
        else:
            bitVector = bitVector & ~shift
    return bitVector & (bitVector - 1) == 0
