# # analysis:
# #     try to find the global min and maxium where the global min comes before global max：
# import math
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         sell, buy = 0, math.inf
#         sid, bid = 0 
#         profit = 0
#         for i in range(len(prices)):
#             if prices[i] < buy:
#                 sell = prices[i]
#                 buy = prices[i]
#                 sid, bid = i
#             elif prices[i] > sell:
#                 sell = prices[i]
#                 new_profit = sell - buy
#                 if new_profit > profit:
#                     profit = new_profit
#                     sid = i
#         for i in range(bid+1,sid):
#             if prices[i] > buy:
#                 sub_diff = prices[i] - buy
                    
            
#         return getSubPrice(prices,bid,sid+1)
        
#     def getSubPrice(self , prices,start,end):
#         if not prices[start:end]:
#             return 0
#         if end - start <= 1:
#             return 0
#         max_profit = 0            
#         for i in range(start, end):
#             init_price = prices[i]
#             for j in range(i+1, end):
#                 if prices[j] > init_price:
#                     cur_dif = prices[j] - init_price
#                     res_dif = self.getSubPrice(prices, j+1, end)
#                     if res_dif + cur_dif > max_profit:
#                         max_profit = res_dif + cur_dif
#         return max_profit

        
# class Solution {
#     public int maxProfit(int[] prices) {
#         int maxprofit = 0;
#         for (int i = 1; i < prices.length; i++) {
#             if (prices[i] > prices[i - 1])
#                 maxprofit += prices[i] - prices[i - 1];
#         }
#         return maxprofit;
#     }
# }

## surprisingly simple solution
            


        