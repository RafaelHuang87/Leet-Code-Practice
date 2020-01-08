class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        total = 0
        dp = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                d = A[i] - A[j]
                if d in dp[i]:
                    dp[i][d] += 1
                else:
                    dp[i][d] = 1
                if d in dp[j]:
                    dp[i][d] += dp[j][d]
                    total += dp[j][d]
        return total
