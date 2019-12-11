class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        N = len(s)
        for i in range(N):
            cur = s[i: i + 10]
            if cur in seen:
                repeated.add(cur)
            else:
                seen.add(cur)
        return list(repeated)
