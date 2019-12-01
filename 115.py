class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = []
        for i in range(len(s) + 1):
            dp.append([0] * (len(t) + 1))
        dp[0][0] = 1
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for a in range(1, len(t) + 1):
            for b in range(a, len(s) + 1):
                if s[b - 1] == t[a - 1]:
                    dp[b][a] = dp[b - 1][a - 1] + dp[b - 1][a]
                else:
                    dp[b][a] = dp[b - 1][a]
        return dp[-1][-1]