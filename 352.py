class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []

    def addNum(self, val: int) -> None:
        import bisect
        m = bisect.bisect(self.d, val)

        if m % 2 == 0:
            if m < len(self.d) and self.d[m] - val == 1:
                self.d[m] = val
            else:
                self.d.insert(m, val)
                self.d.insert(m, val)
            if m > 0 and self.d[m] - self.d[m - 1] <= 1:
                self.d.pop(m)
                self.d.pop(m - 1)

    def getIntervals(self) -> List[List[int]]:
        return [*zip(self.d[:: 2], self.d[1:: 2])]

    # Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()