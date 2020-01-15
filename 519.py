class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.m = n_rows
        self.n = n_cols
        self.total = self.m * self.n - 1
        self.start = 0
        self.fliped = set()

    def flip(self) -> List[int]:
        import random
        while True:
            position = random.randint(self.start, self.total)
            if position not in self.fliped:
                self.fliped.add(position)
                return divmod(position, self.n)

    def reset(self) -> None:
        self.fliped = set()
# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()