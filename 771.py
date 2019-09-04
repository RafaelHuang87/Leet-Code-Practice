"""
Solution for Leet Code 771.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = 0
        for j in range(len(J)):
            for s in range(len(S)):
                if S[s] == J[j]:
                    i += 1
        return i