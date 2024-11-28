class Solution:
    def maxProfit(self, prices):
        # Initialize variables for minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Loop through the prices
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold at the current price
            profit = price - min_price
            # Update the maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit

        