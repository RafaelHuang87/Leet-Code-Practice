class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        elif len(a) == len(b) and a == b:
            return -1
        else:
            return len(a)
