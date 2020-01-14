class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        sum1 = [[0 for i in range(len(nums))] for i in range(len(nums))]
        dp = [[0 for i in range(len(nums) + 1)] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum1[i][j] = sum(nums[:j + 1]) - sum(nums[:i])
        for k in range(1, len(nums)):
            for i in range(len(nums) - k):
                j = i + k
                dp[i][j] = max(nums[i] + sum1[i + 1][j] - dp[i + 1][j], nums[j] + sum1[i][j - 1] - dp[i][j - 1])
            # print dp
        tmp = dp[0][len(nums) - 1]
        if tmp * 2 >= total:
            return True
        else:
            return False
