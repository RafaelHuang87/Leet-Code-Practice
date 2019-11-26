class Solution:
    def mySqrt(self, x: int) -> int:
        def newton(x, x0=0.0001, e=1e-6):
            x_n = 0.5 * (x0 + x / x0)
            while abs(x_n - x0) > e:
                x0 = x_n
                x_n = 0.5 * (x0 + x / x0)
            return x_n

        return int(newton(x))

s = Solution()
print(s.mySqrt(8))