class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix, p = 1, 1
        while p < k:
            count, cur, net = 0, prefix, prefix + 1
            while cur <= n:
                count += min(n + 1, net) - cur
                cur *= 10
                net *= 10
            if p + count <= k:
                prefix += 1
                p += count
            else:
                prefix *= 10
                p += 1
        return prefix
