class Solution:
    def minPatches(self, nums: [int], n: int) -> int:
        patch_count, index, miss = 0, 0, 1
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                patch_count += 1
        return patch_count

s = Solution()
print(s.minPatches([1, 5, 10], 20))