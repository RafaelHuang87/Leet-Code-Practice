class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True

        s_len = len(s1)
        f = self.isScramble
        for i in range(1, s_len):
            if f(s1[i:], s2[i:]) and f(s1[:i], s2[:i]):
                return True
            if f(s1[i:], s2[:s_len - i]) and f(s1[:i], s2[s_len - i:]):
                return True
        return False

s = Solution()
print(s.isScramble('great', 'rgeat'))
