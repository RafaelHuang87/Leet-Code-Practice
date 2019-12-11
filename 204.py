class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        nums = [None] * n
        nums[0], nums[1] = False, False
        for i in range(n):
            if not nums[i]:
                nums[i] = True
                for j in range(i + i, n, i):
                    nums[j] = False
        return sum(nums)