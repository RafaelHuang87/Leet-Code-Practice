class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n >= 5:
            n = n // 5
            r += n
        return r

s = Solution()
print(s.trailingZeroes(8452))