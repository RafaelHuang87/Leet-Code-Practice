class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        l, r = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = l
            l *= nums[i]
        for i in range(len(nums))[::-1]:
            res[i] *= r
            r *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf([1,2,3,4]))
