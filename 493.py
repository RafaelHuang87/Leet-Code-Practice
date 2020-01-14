class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        import bisect
        a = []
        ret = 0
        for x in nums[::-1]:
            ret += bisect.bisect_left(a,x/2)
            bisect.insort(a,x)
        return ret