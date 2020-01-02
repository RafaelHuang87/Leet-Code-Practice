class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        t = n - k
        if n == k:
            return '0'
        res = ''
        for i in range(n):
            while k and res and res[-1] > num[i]:
                res = res[:-1]
                k -= 1
            res += num[i]
            if k == 0:
                res += num[i + 1:]
                break
        res = res[:t]
        for i in range(len(res)):
            if res[i] != '0':
                return res[i:] if res[i:] else '0'
        return '0'