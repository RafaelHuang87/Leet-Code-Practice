class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = [1, 2]
        for i in range(2, n):
            count.append(count[i - 1] + count[i - 2])
        return count[-1]


s = Solution()
print(s.climbStairs(35))