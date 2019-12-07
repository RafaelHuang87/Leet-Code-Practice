class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxvalue = minvalue = nums[0]
        globalmax = nums[0]
        for i in range(1, len(nums)):
            lastmax = maxvalue
            maxvalue = max(minvalue * nums[i], lastmax * nums[i], nums[i])
            minvalue = min(minvalue * nums[i], lastmax * nums[i], nums[i])
            globalmax = max(globalmax, maxvalue)
        return globalmax
