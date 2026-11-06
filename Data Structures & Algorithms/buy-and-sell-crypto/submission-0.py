class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = float("inf")
        max_stock = 0
        for price in prices:
            if price < min_stock:
                min_stock = price
            elif price - min_stock > max_stock:
                max_stock = price - min_stock
        return max_stock             

        