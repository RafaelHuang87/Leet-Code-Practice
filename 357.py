class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res, con = 10, 9
        for i in range(1, n):
            res += con * (10 - i)
            con *= (10 - i)
        return res