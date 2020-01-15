class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        rec = {}
        for i, val in enumerate(ring):
            if val not in rec:
                rec[val] = []
            rec[val].append(i)
        leng = len(ring)
        past = [(0, 0)]
        for c in key:
            cur = []
            for j in rec[c]:
                minval = float('inf')
                for pasti, m in past:
                    temp = abs(j - pasti)
                    minval = min(minval, m + temp, m + leng - temp)
                cur.append((j, minval))
            past = cur
        return min([x[1] for x in past]) + len(key)
