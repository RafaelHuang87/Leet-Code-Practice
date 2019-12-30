class Solution:

    def __init__(self, nums: List[int]):
        self.orgin = nums[:]
        self.output = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orgin


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        n = len(self.output)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()