class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0
        n, res, mysum = len(A), 0, 0
        for i in range(n):
            res += i * A[i]
            mysum += A[i]
        pre = res
        for j in range(n - 1, 0, -1):
            pre = pre + mysum - n * A[j]
            res = max(res, pre)
        return res
