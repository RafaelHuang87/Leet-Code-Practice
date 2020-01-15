class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if s == s[::-1]:
            return n
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            tmp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    tmp[j][i] = 2 + tmp[j + 1][i - 1]
                else:
                    tmp[j][i] = max(tmp[j + 1][i], tmp[j][i - 1])
        return tmp[0][n - 1]
