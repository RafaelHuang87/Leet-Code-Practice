class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        max_cons = 0
        temp = 0
        for val in nums:
            if val == 1:
                temp += 1
            else:
                max_cons = max(max_cons, temp)
                temp = 0
        max_cons = max(max_cons, temp)
        return max_cons

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
