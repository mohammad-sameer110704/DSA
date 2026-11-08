class Solution(object):
    def maxProfit(self, prices):
        minBuy = float('inf')
        profit = 0

        for price in prices:
            if price < minBuy:
                minBuy = price
            elif price - minBuy > profit:
                profit = price - minBuy

        return profit