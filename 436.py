class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        invs = sorted((x[0], i) for i, x in enumerate(intervals))
        ans = []
        for x in intervals:
            idx = bisect.bisect_right(invs, (x[1],))
            ans.append(invs[idx][1] if idx < len(intervals) else -1)
        return ans
