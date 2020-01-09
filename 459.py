class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                a, j = s[:i], i
                while j < n and s[j:j + i] == a:
                    j += i
                if j == n: return True

        return False