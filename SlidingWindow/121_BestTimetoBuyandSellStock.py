# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


## Solution: Time Complexity: O(n); Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]; maximum=0
        for i in range(1,len(prices)):
            curr_profit=prices[i]-buy_price
            if (maximum<curr_profit):
                maximum=curr_profit
            if (prices[i]<buy_price):
                buy_price=prices[i]
                
        return maximum
