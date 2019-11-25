class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if newInterval == []:
            return intervals
        res = []
        intervals.append(newInterval)
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
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))