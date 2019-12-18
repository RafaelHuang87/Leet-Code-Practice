class Solution:
    def addDigits(self, num: int) -> int:
        nums = str(num)
        while len(nums) != 1:
            temp = 0
            for val in nums:
                temp += int(val)
            nums = str(temp)
        return int(nums)
    # Optimization: return num and (num % 9 or 9)

s = Solution()
print(s.addDigits(38))