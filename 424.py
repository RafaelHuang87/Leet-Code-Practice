class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        import collections
        count = collections.Counter()
        res = 0
        start = 0
        for i, char in enumerate(s):
            count[char] += 1
            maxCnt = count.most_common(1)[0][1]
            while i - start + 1 - maxCnt > k:
                count[s[start]] = count[s[start]] - 1
                start += 1
            res = max(res, i - start + 1)
        return res
