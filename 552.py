class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3

        poss = [1, 2, 4]
        for i in range(2, n):
            poss.append((poss[i] + poss[i-1] + poss[i-2]) % 1000000007)
        res = poss[n]
        for i in range(n):
            res = (res + poss[i] * poss[n-i-1]) % 1000000007
        return res