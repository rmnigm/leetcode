class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = None
        profit = 0
        for p in prices:
            if prev is not None and p > prev:
                profit += (p - prev)
            prev = p
        return profit