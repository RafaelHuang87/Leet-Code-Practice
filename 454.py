class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import defaultdict
        map1 = defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                t = a + b
                map1[t] += 1

        for c in C:
            for d in D:
                t = - c - d
                res += map1[t]

        return res
