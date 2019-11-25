class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 0
        elif n < 0:
            return (1.0 / x) ** abs(n)
        else:
            return x ** n

s = Solution()
print(s.myPow(2.00000, 10))