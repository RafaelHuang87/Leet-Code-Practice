class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right, insort
        if not nums or upper < lower:
            return 0
        p = [0]
        for a in nums:
            p.append(p[-1] + a)
        walked = []
        ans = 0
        for a in p[::-1]:
            l, r = a + lower, a + upper
            i, j = bisect_left(walked, l), bisect_right(walked, r)
            ans += j - i
            insort(walked, a)
        return ans