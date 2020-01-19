class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            if self.subseq(word, s):
                return word
        return ""

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

