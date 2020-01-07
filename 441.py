class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            if 0 <= n - (mid + 1) * mid // 2 < mid + 1:
                return mid
            elif n - (mid + 1) * mid // 2 >= mid + 1:
                low = mid + 1
            elif n - (mid + 1) * mid // 2 < 0:
                high = mid - 1
