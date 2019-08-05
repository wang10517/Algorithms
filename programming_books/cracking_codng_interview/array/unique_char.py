# Assuming the string consists of only ascii chars
# def hasUniqueChar(string):
#     charSet = [0 for i in range(128)]
#     for char in string:
#         if charSet[ord(char)]:
#             return False
#         else:
#             charSet[ord(char)] = 1
#     return True

# assuming only a thorugh z
# since the int type has a max limit
# this only allows checking in the range of 2^n where n is the number of possible characters in the character set


def hasUniqueChar(string):
    checker = 0
    for char in string:
        if checker & (1 << (ord(char)-ord('a'))) > 0:
            return False
        checker = checker | (1 << (ord(char)-ord('a')))
    return True
