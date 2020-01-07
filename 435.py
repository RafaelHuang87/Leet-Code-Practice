class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        last, res = 0, 0
        for i in range(1, len(intervals)):
            if intervals[last][1] > intervals[i][0]:
                if intervals[i][1] < intervals[last][1]:
                    last = i
                res += 1
            else:
                last = i
        return res

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))