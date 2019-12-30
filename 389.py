class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sumt, sums = 0, 0
        for t1 in t:
            sumt += ord(t1)
        for s1 in s:
            sums += ord(s1)
        return chr(sumt - sums)
