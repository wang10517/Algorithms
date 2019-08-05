import math
import sys

def isPowerOfThree(n: int) -> bool:
    while x >= base:
        remainder = x % base
        if remainder != 0:
            return False
        x = x // base
    if x == 1 :
        return True
    else:
        return False

if __name__ == "__main__":
    isPowerOfThree(243)


## 1162261467 largest power of three under max int by taking 3 to the power of floor of log3 of max int

# public class Solution {
#     public boolean isPowerOfThree(int n) {
#         return n > 0 && 1162261467 % n == 0;
#     }
# }
