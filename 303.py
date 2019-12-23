class NumArray:

    def __init__(self, nums: [int]):
        self.nums_dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.nums_dp[i] = self.nums_dp[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums_dp[j+1] - self.nums_dp[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)