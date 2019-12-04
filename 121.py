class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        result = 0
        minimum = prices[0]
        for price in prices:
            minimum = min(price, minimum)
            result = max(price - minimum, result)
        return result

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))