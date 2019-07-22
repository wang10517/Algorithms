# analysis:
#     try to find the global min and maxium where the global min comes before global max：
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        sell, buy = 0, math.inf 
        profit = 0
        for p in prices:
            if p < buy:
                sell = p
                buy = p
            elif p > sell:
                sell = p
                profit = max(sell - buy, profit)
        return profit
            


        