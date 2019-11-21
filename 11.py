class Solution:
    def maxArea(self, height) -> int:
        if not height or len(height) == 1:
            return 0
        l = 0
        r = len(height) - 1
        res = abs(r - l) * (min(height[l], height[r]))

        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * abs(r - l))
                l += 1
            else:
                res = max(res, height[r] * abs(r - l))
                r -= 1
        return res

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
