class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def pick(self, target: int) -> int:
        import random
        res = []
        for i in range(self.n):
            if self.nums[i] == target:
                res.append(i)
        return random.choice(res)
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)