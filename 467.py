class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) < 1:
            return 0
        dp = [0] * 26
        dp[ord(p[0]) - 97] += 1
        curlen = 1
        for i in range(1, len(p)):
            d = ord(p[i]) - 97
            if d - ord(p[i - 1]) + 97 == 1 or d - ord(p[i - 1]) + 97 == -25:  # 如果是下一个字母
                curlen += 1
                dp[d] = max(curlen, dp[d])
            else:
                curlen = 1
                dp[d] = max(dp[d], 1)
        return sum(dp)
