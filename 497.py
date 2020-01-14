class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weight = []
        s = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            s += area
            self.weight.append(s)

    def pick(self) -> List[int]:
        import bisect
        import random
        index = bisect.bisect_left(self.weight, random.randint(1, self.weight[-1]))
        rect = self.rects[index]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()