class Solution:
    def maxProduct(self, words: List[str]) -> int:
        import collections
        res = 0
        d = collections.defaultdict(int)
        N = len(words)
        for i in range(N):
            w = words[i]
            for c in w:
                d[w] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[j]] & d[words[i]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res
