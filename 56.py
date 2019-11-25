class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals = sorted(intervals)
        l = intervals[0][0]
        h = intervals[0][-1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= h:
                h = max(h, intervals[i][-1])
            else:
                res.append([l, h])
                l = intervals[i][0]
                h = intervals[i][-1]
        res.append([l, h])
        return res



s = Solution()
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
