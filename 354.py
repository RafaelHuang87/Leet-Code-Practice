

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left

        if not envelopes:
            return 0
        envelopes.sort(key=lambda a: (a[0], -a[1]))
        mem = list()
        for e in envelopes:
            index = bisect_left(mem, e[1])
            if len(mem) == index:
                mem.append(e[1])
            else:
                mem[index] = e[1]
        return len(mem)