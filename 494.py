class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_nums = sum(nums)
        if sum_nums < S or (S + sum_nums)%2 != 0:
            return 0

        target = (S + sum_nums) >> 1
        mem = [0]*(target + 1)
        mem[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                mem[i] += mem[i - num]
        return mem[target]
