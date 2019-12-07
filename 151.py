class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        res = ' '
        return res.join(words)

s = Solution()
print(s.reverseWords("  hello world!  "))