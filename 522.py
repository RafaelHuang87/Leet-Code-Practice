class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        from collections import Counter
        c = Counter(strs)
        dstrs = sorted(c.keys(), key=len, reverse=True)
        for i, w in enumerate(dstrs):
            if c[w] == 1 and all(not self.subseq(w, s) for s in dstrs[:i]):
                return len(w)
        return -1

    def subseq(self, a, b):
        if not (len(a) <= len(b) and set(a) <= set(b)):
            return False
        i = 0
        n = len(a)
        for c in b:
            if i < n:
                if c == a[i]:
                    i += 1
            else:
                break
        return i == n
