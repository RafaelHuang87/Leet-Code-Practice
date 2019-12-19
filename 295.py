import bisect


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_list = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.num_list, num)

    def findMedian(self) -> float:
        if len(self.num_list) % 2 == 0:
            return (self.num_list[len(self.num_list) // 2] + self.num_list[(len(self.num_list) - 1) // 2]) / 2.
        else:
            return self.num_list[len(self.num_list) // 2] / 1.
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)