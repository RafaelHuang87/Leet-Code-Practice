class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [(i - 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
s = Solution()
print(s.minCut("aab"))