class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 1 << 31 - 1
        if dividend == 0:
            return 0
        i = 0
        res = 0
        p = abs(dividend)
        q = abs(divisor)

        while q << i <= p:
            i = i + 1

        for j in reversed(range(i)):
            if q << j <= p:
                p -= q << j
                res += 1 << j

        if (dividend > 0) != (divisor > 0) or res < -1 << 31:
            res = -res
        return min(res, 1 << 31 - 1)

s = Solution()
print((1 << 31) - 1)