class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n, res = len(prices), 0
        if n < 2:
            return 0
        if k > n // 2:
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        hold, sold = [float('-inf')] * (k + 1), [0] * (k + 1)
        for price in prices:
            for j in range(1, k + 1):
                hold[j] = max(hold[j], sold[j - 1] - price)
                sold[j] = max(sold[j], hold[j] + price)
        return sold[k]
