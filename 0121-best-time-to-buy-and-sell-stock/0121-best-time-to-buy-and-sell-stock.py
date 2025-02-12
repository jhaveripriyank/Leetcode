class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        buy_price = 10001
        for idx, price in enumerate(prices):
            if price < buy_price:
                buy_price = price
                continue
            else:
                current_profit = price - buy_price 
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit