"""
LC121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell idx > buy idx
        # only one trade
        # find the max sell_value - buy_value
        max_profit = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            # check1: buy price < min price
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit


"""
[7,1,5,3,6,4]
mb = 7 mp = 0
mb = 1 mp=0
mb = 1 mp = 4
mb =1 mp = 4
mb =1 mp =5
mb=1 mp = 5
return 5

[7,6,4,3,1]
mb =7 mp =0 
mb =6 mp = 0
mb = 4 mp = 0
mb =3 mp = 0
mb =1 mp = 0
return 0
"""
