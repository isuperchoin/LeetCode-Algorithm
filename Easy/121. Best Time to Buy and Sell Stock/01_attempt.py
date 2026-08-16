#================================
# Working process:
#   1. Create a variable to keep track of the minimum price and set it to infinity
#   2. Create a variable to keep track of the maximum profit and set it to 0
#   3. Loop through the prices list, keep updating the minimum price and maximum profit
#   4. Return the maximum profit
# TakeAway: Greedy algorithm, keep track of the minimum price and maximum profit while iterating through the list
#================================



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i

            if max_profit < i - min_price:
                max_profit = i - min_price
            
        return max_profit