class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i

        return False
